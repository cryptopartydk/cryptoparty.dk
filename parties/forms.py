from django import forms
from .models import Party


class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = ['title', 'description', 'when', 'venue',
                  'address', 'city', 'postal_code', 'public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'when': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
