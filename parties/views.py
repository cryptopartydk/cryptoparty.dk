from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    TemplateView,
)
from paloma import TemplateMail
from cryptoparty.mixins import LoginRequiredMixin

from .models import Party, Venue
from .forms import PartyForm


def process_form(self, form, subject=None, template_name=None):
    venue = form.cleaned_data.get('venue')
    venue_name = form.cleaned_data.get('venue_name')
    venue_address = form.cleaned_data.get('venue_address')

    party = form.save(commit=False)

    party_is_new = not bool(party.id)

    if not venue and venue_name:
        party.venue = Venue.objects.create(
            name=venue_name,
            address=venue_address,
        )

    party.save()

    if party_is_new:
        party.organizers.add(self.request.user)
        party.save()

    context = {
        'host': self.request.META.get('HTTP_HOST'),
        'party': party
    }

    if subject and template_name:
        mail = TemplateMail(
            subject=subject,
            text_template_name=template_name,
        )
        mail.send(
            to=self.request.user.email,
            context=context
        )

    return HttpResponseRedirect(
        reverse_lazy(
            'parties:party-detail',
            kwargs={'slug': party.slug}
        )
    )


class PartyList(TemplateView):
    model = Party
    template_name = 'parties/party_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_parties'] = Party.objects.upcoming().public()
        context['past_parties'] = Party.objects.past().public()
        return context


class PartyDetail(DetailView):
    model = Party
    template_name = 'parties/party_detail.html'
    context_object_name = 'party'

    def dispatch(self, request, *args, **kwargs):
        party = self.get_object()
        if not party.public and request.user not in party.organizers.all():
            raise Http404
        return super().dispatch(
            request,
            *args,
            **kwargs
        )


class PartyUpdate(LoginRequiredMixin, UpdateView):
    model = Party
    template_name = 'parties/party_form.html'
    form_class = PartyForm

    def form_valid(self, form):
        return process_form(self, form)


class PartyCreate(LoginRequiredMixin, CreateView):
    model = Party
    template_name = 'parties/party_form.html'
    form_class = PartyForm

    def form_valid(self, form):
        return process_form(
            self,
            form,
            subject='Your cryptoparty has been created!',
            template_name='parties/email/new_party.txt',
        )
