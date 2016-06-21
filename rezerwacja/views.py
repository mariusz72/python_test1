from django.shortcuts import render
from django.core.mail import send_mail

from django.template import RequestContext
from django.shortcuts import render_to_response
from rezerwacja.models import Rezerwacje
from .forms import TestForm


def index(request):
    form = TestForm()

    if request.method == "POST":
      zmienna_post = 'po zapisie'
      form = TestForm(request.POST)
    
      if form.is_valid():
	 zmienna_post = 'zwalidowane'
	 post = form.save()
	 
         message = 'Zarezerwowano stolik nr:'+request.POST['stolik']+' w terminie '+request.POST['od']+' - '+request.POST['do']
	 sendto = [request.POST['email']]
	 
         send_mail(
          'Potwierdzenie rezerwacji',
          message,
          'from@example.com',
          sendto,
          fail_silently=False,
         )	 

	 return render_to_response('zapis.html',
            {
              'zmienna':request.POST, 
              'cena':int(request.POST['ileosob'])*5,
             },
            context_instance=RequestContext(request)
            )
            
    else:
      zmienna_post = 'przed zapisem'       
    
      return render_to_response('index.html',
            {
              'zmienna':zmienna_post, 
              'form':form,
             },
            context_instance=RequestContext(request)
            )
         


