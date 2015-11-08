import re
from django import forms
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
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.TextInput(attrs={'class': 'form-control'}),
            'end': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

