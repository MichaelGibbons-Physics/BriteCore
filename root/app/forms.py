from django import forms
from . import models

class InsuranceForm(forms.ModelForm):
    class Meta:
        model=models.Insurance
        fields=['riskType','fieldName','fieldData','fieldType','enumType']
