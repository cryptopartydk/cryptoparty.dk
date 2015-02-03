import json
from django.contrib import messages
from django.core.serializers import serialize
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import CreateView, ListView, DetailView, FormView, \
    View

from .models import Party
from .forms import AttendeeForm
from .templatetags.cryptoparty_tags import markup


class PartyList(ListView):
    model = Party
    template_name = 'parties/party_list.html'
    context_object_name = 'parties'


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
        messages.info(self.request, 'You are now signed up!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('parties:party-detail',
                            kwargs={'slug': self.get_object().slug})


class PartyCreate(CreateView):
    model = Party
    template_name = 'parties/party_form.html'
    success_url = reverse_lazy('parties:party-list')


class PartyAjaxUpdate(View):

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = Party.objects.get(pk=kwargs.get('pk'))
        obj.description = request.POST.get('description', obj.description)
        obj.save()

        data = {
            'description': markup(obj.description)
        }

        return HttpResponse(status=200, content=json.dumps(data))
