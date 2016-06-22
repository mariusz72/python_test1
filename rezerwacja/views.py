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
         stolik = Stoliki.objects.get(nr_stolika=request.POST['stolik'])
         types_list = Rezerwacje.objects.filter(Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now()))
         #types_list = Rezerwacje.objects.filter(nazwisko='wewe')
         #entry = types_list.all()[1].od # some previous entry 
         entry = types_list.all().count()

         zakres='null' 
         rezerwacja_lista = Rezerwacje.objects.filter((Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now())) & Q(stolik=request.POST['stolik']) )
         if rezerwacja_lista.all().count()>0:
            for item in rezerwacja_lista:
             if u'%s' % (request.POST['od']) <= u'%s' % (item.do) and u'%s' % (request.POST['do']) >=u'%s' % (item.od): 
		od_do=u'%s' % (item.od)+' - '+u'%s' % (item.do)
                zakres='empty'
                break

         
         if int(request.POST['ileosob']) > int(stolik.ile_osob):
             alert = 'Przekroczona ilosc osob dla wybranego stolika, max='+str(stolik.ile_osob)
         elif zakres=='empty':
              e = datetime.datetime.strptime(request.POST['do'], "%Y-%m-%d %H:%M")
              c = datetime.datetime.strptime(request.POST['od'], "%Y-%m-%d %H:%M")
              timediff = e-c
              alert = 'Stolik nr:'+request.POST['stolik']+' jest zajety w terminie '+od_do
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
         


