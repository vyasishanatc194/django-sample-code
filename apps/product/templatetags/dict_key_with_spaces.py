from django import template
register = template.Library()

@register.filter(is_safe=True)
def dict_with_space(value, arg):
  return value[arg]