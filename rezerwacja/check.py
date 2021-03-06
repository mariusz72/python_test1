from rezerwacja.models import Rezerwacje
from rezerwacja.models import Stoliki
from datetime import date
import datetime
from django.db.models import Q

def where_empty(post):

    sto_list = Stoliki.objects.filter(Q(ile_osob__gte=post['ileosob']))
    
    for sto in sto_list:
        
        rezerwacja_lista = Rezerwacje.objects.filter((Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now())) & Q(stolik=sto.nr_stolika) )
        if rezerwacja_lista.all().count()<=0:
           return sto.nr_stolika
        else:
           for item in rezerwacja_lista:
               if u'%s' % (post['do']) <= u'%s' % (item.od) or u'%s' % (post['od']) >=u'%s' % (item.do): 
                  return sto.nr_stolika
    return 0

def is_busy(post):

    types_list = Rezerwacje.objects.filter(Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now()))

    rezerwacja_lista2 = Rezerwacje.objects.filter((Q(od__gt=datetime.datetime.now()) | Q(do__gt=datetime.datetime.now())) & Q(stolik=post['stolik']) )
    if rezerwacja_lista2.all().count()>0:
       for item in rezerwacja_lista2:
           if u'%s' % (post['od']) <= u'%s' % (item.do) and u'%s' % (post['do']) >=u'%s' % (item.od): 
	     od_do=u'%s' % (item.od)+' - '+u'%s' % (item.do)
             return 'busy'
    else:
       return 'busy'

    return 'empty'
 
