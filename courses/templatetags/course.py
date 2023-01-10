"""access the model name from here since django does not allow direct 
access of underscore(__) methods from the template"""

from django import template

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
