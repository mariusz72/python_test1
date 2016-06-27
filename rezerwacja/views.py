from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.mail import send_mail
from datetime import date
import datetime
from django.db.models import Q
import json
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response
from rezerwacja.models import Rezerwacje
from rezerwacja.models import Stoliki
from rezerwacja.email import send_email
from rezerwacja.check import where_empty
from rezerwacja.check import is_busy
from .forms import TestForm


def index(request):
   form = TestForm()
   wolny = 0
   if request.method == "POST":
      form = TestForm(request.POST)
    
      if form.is_valid():
   
	 #walidacja
         stolik = Stoliki.objects.get(nr_stolika=request.POST['stolik'])
         types_list = Rezerwacje.objects.filter(Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now()))

         zakres='null' 
         rezerwacja_lista = Rezerwacje.objects.filter((Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now())) & Q(stolik=request.POST['stolik']) )
         if rezerwacja_lista.all().count()>0:
            for item in rezerwacja_lista:
             if u'%s' % (request.POST['od']) <= u'%s' % (item.do) and u'%s' % (request.POST['do']) >=u'%s' % (item.od): 
		od_do=u'%s' % (item.od)+' - '+u'%s' % (item.do)
                zakres='busy'
                break

         
         if int(request.POST['ileosob']) > int(stolik.ile_osob):
             alert = 'Przekroczona ilosc osob dla wybranego stolika, max='+str(stolik.ile_osob)
         elif zakres=='busy':
	      #### busy
	      wolny = where_empty(request.POST)
              alert = 'Stolik nr:'+request.POST['stolik']+' jest zajety w terminie '+od_do
         else:
            alert = 0
        
      return render_to_response('akcept.html',
            {
              'alert':alert,
              'zmienna':request.POST, 
              'cena':int(request.POST['ileosob'])*5,
              'wolny':wolny,
             },
            context_instance=RequestContext(request)
            )
   else:
      return render_to_response('index.html',
            {
              'form':form,
             },
            context_instance=RequestContext(request)
            )
         
def zapisz_rez(request):
    form = request.POST

    post = Rezerwacje(imie=form['imie'], 
                  nazwisko=form['nazwisko'],
                  email=form['email'],
                  od=form['od'],
                  do=form['do'],
                  stolik=form['stolik'],
                  ileosob=form['ileosob'],
    )

    if is_busy(request.POST)=='busy':
       post.save()
       message = 'Zarezerwowano stolik nr:'+request.POST['stolik']+' w terminie '+request.POST['od']+' - '+request.POST['do']
       email = {}		
       email['subject'] = 'Potwierdzenie rezerwacji'
       email['message'] = message
       email['from_email'] = request.POST['email']

       ####################### 
       #   send_email(email)
    
       return HttpResponse(message, content_type="application/json")
    else:
       return HttpResponse("Termin zajety!", status=404)






