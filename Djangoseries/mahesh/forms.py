from django import forms
from .models import ComputerVarity

class ComputerVarityForm(forms.Form):
    computer_variety = forms.ModelChoiceField(queryset=ComputerVarity.objects.all(),label='Select Computer Variety')
    