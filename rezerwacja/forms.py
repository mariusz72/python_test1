from django import forms        
from rezerwacja.models import Rezerwacje

class TestForm(forms.ModelForm):

    class Meta:
        model = Rezerwacje
        fields = ('imie', 'nazwisko', 'email', 'od', 'do', 'stolik', 'ileosob')
        