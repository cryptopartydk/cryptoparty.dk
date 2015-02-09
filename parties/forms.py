from django import forms
from .models import Party, Attendee


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['title', 'description', 'when', 'venue',
                  'address', 'city', 'postal_code', 'creator_email']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'when': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'creator_email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'crypto_level']


