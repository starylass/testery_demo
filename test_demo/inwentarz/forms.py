from django import forms
from .models import *


class testerForm(forms.ModelForm):
    class Meta:
        model = Tester
        fields = ('phandlowy', 'data_wypozyczenia')
