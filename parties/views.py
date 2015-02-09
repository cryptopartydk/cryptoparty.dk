import json
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView, DetailView, FormView, View
from django.utils.translation import ugettext_lazy as _
from paloma import TemplateMail

from .models import Party
from .forms import AttendeeForm, PartyForm
from .templatetags.cryptoparty_tags import markup


class PartyList(CreateView):
    model = Party
    template_name = 'parties/party_list.html'
    form_class = PartyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_parties'] = Party.objects.upcoming().public()
        context['past_parties'] = Party.objects.past().public()
        return context

    def form_valid(self, form):
        self.object = form.save()

        context = {
            'host': self.request.META.get('HTTP_HOST'),
            'party': self.object
        }

        if self.object.creator_email:
            mail = TemplateMail(
                subject=_('Your cryptoparty has been created!'),
                from_email='contact@cryptoparty.dk',
                from_name='Cryptoparty.dk',
                text_template_name='parties/email/new_party.txt',
            )

            mail.send(
                to=self.object.creator_email,
                context=context
            )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            'parties:party-detail-with-key',
            kwargs={'slug': self.object.slug, 'key': self.object.key}
        )


class PartyDetail(FormView, DetailView):
    model = Party
    template_name = 'parties/party_detail.html'
    context_object_name = 'party'
    form_class = AttendeeForm

    def get_context_data(self, **kwargs):
        # Somehow the object falls of the view... TODO: Find out why
        self.object = self.get_object()

        context = super().get_context_data(**kwargs)

        key = self.request.GET.get('key', None)

        context['valid_key'] = False
        if key == self.object.key:
            context['valid_key'] = True

        context['form'] = self.get_form(self.get_form_class())
        return context

    def form_valid(self, form):
        attendee = form.save(commit=False)
        attendee.party = self.get_object()
        attendee.save()
        messages.info(self.request, _('You are now signed up!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('parties:party-detail',
                            kwargs={'slug': self.get_object().slug})


class PartyCreate(CreateView):
    model = Party
    template_name = 'parties/party_form.html'
    success_url = reverse_lazy('parties:party-list')
    form_class = PartyForm


class PartyAjaxUpdate(View):

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = Party.objects.get(pk=kwargs.get('pk'))
        data = {}

        if obj.key == request.POST.get('key'):
            toggle_public = request.POST.get('public', None)
            if toggle_public:
                obj.public = not obj.public
                obj.save()
                data['public'] = obj.public
            else:
                obj.description = request.POST.get('description', obj.description)
                obj.title = request.POST.get('title', obj.title)
                obj.when = request.POST.get('when', obj.when)
                obj.address = request.POST.get('address', obj.address)
                obj.venue = request.POST.get('venue', obj.venue)
                obj.city = request.POST.get('city', obj.city)

                postal_code = request.POST.get(
                    'postal_code', obj.postal_code)
                if postal_code:
                    obj.postal_code = postal_code

                obj.save()

                data['description'] = markup(obj.description)

            data['updated_at'] = obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')

            return HttpResponse(status=200, content=json.dumps(data))

        return HttpResponse(status=403)
