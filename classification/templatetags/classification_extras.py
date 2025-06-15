from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return float(value) * float(arg)

@register.filter(name='split')
def split(value, separator=','):
    """
    Custom template filter to split a string into a list
    """
    return value.split(separator)