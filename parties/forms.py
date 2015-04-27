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
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'when': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

