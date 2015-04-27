from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.utils.translation import ugettext_lazy as _
from paloma import TemplateMail

from .models import Party, Venue
from .forms import PartyForm


class PartyList(CreateView):
    model = Party
    template_name = 'parties/party_list.html'
    form_class = PartyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_parties'] = Party.objects.upcoming().public()
        context['past_parties'] = Party.objects.past().public()
        return context


class PartyDetail(DetailView):
    model = Party
    template_name = 'parties/party_detail.html'
    context_object_name = 'party'


class PartyUpdate(UpdateView):
    model = Party
    template_name = 'parties/party_form.html'
    form_class = PartyForm


class PartyCreate(CreateView):
    model = Party
    template_name = 'parties/party_form.html'
    form_class = PartyForm

    def form_valid(self, form):

        venue = form.cleaned_data.get('venue')
        venue_name = form.cleaned_data.get('venue_name')
        venue_address = form.cleaned_data.get('venue_address')

        party = form.save(commit=False)
        if not venue and venue_name:
            party.venue = Venue.objects.create(
                name=venue_name,
                address=venue_address,
            )
        party.save()

        user = self.request.user
        party.organizers.add(user)

        party.save()

        context = {
            'host': self.request.META.get('HTTP_HOST'),
            'party': party
        }

        if hasattr(self.object, 'email'):
            mail = TemplateMail(
                subject=_('Your cryptoparty has been created!'),
                text_template_name='parties/email/new_party.txt',
            )

            mail.send(
                to=user.email,
                context=context
            )

        return HttpResponseRedirect(
            reverse_lazy(
                'parties:party-detail',
                kwargs={'slug': party.slug}
            )
        )
