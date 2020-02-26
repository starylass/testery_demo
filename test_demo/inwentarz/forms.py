from django import forms
from .models import *


class testerForm(forms.ModelForm):
    class Meta:
        model = Tester
        fields = ('phandlowy', 'data_wypozyczenia')


class nowyPhForm(forms.ModelForm):
    class Meta:
        model = Phandlowy
        fields = ('imie', 'nazwisko', 'email', 'telefon', 'firma')
