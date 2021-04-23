from django import forms
from testapp.models import Matche
class MatcheForm(forms.ModelForm):
    class Meta:
        model=Matche
        fields='__all__' 
