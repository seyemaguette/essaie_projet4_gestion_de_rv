from django import forms
from .models import Docteur, Rv, Patient


class DocteurForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Docteur



class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

class RvForm(forms.ModelForm):

    class Meta:
        model = Rv