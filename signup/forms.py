from django import forms
from signup.models import Attendee


class SignupForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
