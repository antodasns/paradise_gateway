from django import template

register = template.Library()

@register.filter(name='int')
def toint(value):
	return int(value)