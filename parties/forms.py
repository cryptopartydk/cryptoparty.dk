import re
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Party, Venue


class PartyForm(forms.ModelForm):

    venue = forms.ModelChoiceField(
        Venue.objects.all(),
        required=False,
        initial=None,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    venue_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    venue_address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'adresse-autocomplete'
            }
        )
    )

    class Meta:
        model = Party
        fields = [
            'title',
            'description',
            'start',
            'end',
            'public',
            'venue',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.TextInput(attrs={'class': 'form-control'}),
            'end': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = self.cleaned_data
        venue = data.get('venue', None)
        venue_name = data.get('venue_name', None)
        venue_address = data.get('venue_address', None)

        if venue:
            return data

        if not venue and not (venue_name and venue_address):
            if venue_name and not venue_address:
                self.add_error('venue_address', _('Address is required.'))

            if not venue_name and venue_address:
                self.add_error('venue_name', _('Name of venue is required.'))

            raise forms.ValidationError(
                _('You have to specify either a venue name and address, or choose an existing venue from the dropdown.')
            )

        return data



