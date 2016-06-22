from django.shortcuts import render
from django.core.mail import send_mail
from datetime import date
import datetime
from django.db.models import Q

from django.template import RequestContext
from django.shortcuts import render_to_response
from rezerwacja.models import Rezerwacje
from rezerwacja.models import Stoliki
from .forms import TestForm


def index(request):
   form = TestForm()

   if request.method == "POST":
      zmienna_post = 'po zapisie'
      form = TestForm(request.POST)
    
      if form.is_valid():
         zmienna_post = 'zwalidowane'
   
	 #walidacja
         stolik = Stoliki.objects.get(nr_stolika=2)
	 #ativRezerwacje = Rezerwacje.objects.filter(od>'2016-06-20 21:00')
         types_list = Rezerwacje.objects.filter(Q(nazwisko='1wewe2') | Q(od__gt=datetime.datetime.now()))
         #types_list = Rezerwacje.objects.filter(nazwisko='wewe')
         #entry = types_list.all()[1].od # some previous entry 
         entry = types_list.all().count()
         #old_authors = entry.nazwisko.all()[1]

         
         if int(request.POST['ileosob']) > int(stolik.ile_osob):
             alert = 'Przekroczona ilosc osob, max='+str(stolik.ile_osob)
         elif request.POST['od'] <> request.POST['do']:
              e = datetime.datetime.strptime(request.POST['do'], "%Y-%m-%d %H:%M")
              c = datetime.datetime.strptime(request.POST['od'], "%Y-%m-%d %H:%M")
              timediff = e-c
              alert = 'Nieprawidlowa data'+ u'%s' % (timediff.total_seconds())+ 'entry ='+ u'%s' % (entry) +' ===>' + u'%s' % (datetime.datetime.now())
         else:
            alert = 0
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
              'alert':alert,
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
         


