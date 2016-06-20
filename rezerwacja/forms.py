from django import forms        
from rezerwacja.models import Rezerwacje, Klienci

#class TestForm(forms.Form):
#	subject = forms.CharField(max_length=100)
#	message = forms.CharField()
#	sender = forms.EmailField()        


class TestForm(forms.ModelForm):

    class Meta:
        model = Rezerwacje
        fields = ('imie', 'nazwisko', 'email', 'od', 'do', 'stolik', 'ileosob')
        
class Test2Form(forms.ModelForm):

    class Meta:
        model = Klienci
        fields = ('imie', 'mazwisko', 'email')        