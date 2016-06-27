from django import template

from django.core.serializers import serialize
from django.db.models.query import QuerySet
import simplejson as json
from django.template import Library


register = template.Library()

@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='add_css_attr')
def addattr(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.as_widget(attrs={'class': arg_list[0], 'required': arg_list[1]})

@register.filter
def to_date(value):
    return value.replace(":00+00:00","")

@register.filter(name='jsonify')
def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return json.dumps(object)


