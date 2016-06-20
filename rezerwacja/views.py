from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response
from rezerwacja.models import Rezerwacje, Klienci
from .forms import TestForm
from .forms import Test2Form


def index(request):
    klient = Klienci.objects.get(id=1)
    klienci = Klienci.objects.all()
    form = TestForm()
    form2 = Test2Form()
    if request.method == "POST":
      zmienna_post = 'po zapisie'
      form = TestForm(request.POST)
      form2 = Test2Form(request.POST)
      
      if form.is_valid():
         post = form.save()
         post2 = form2.save()

      
    else:
      zmienna_post = 'przed zapisem'       
    
    return render_to_response('index.html',
            {
              'zmienna':zmienna_post, 
              'zmienna2':klient,
              'zmienna3':klienci,
              'form':form,
              'form2':form2
             },
            context_instance=RequestContext(request)
            )
         


