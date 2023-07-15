from django import template

register = template.Library()


@register.filter(name="split")
def split(value, key):
    value.split(f"{key}")
    return value.split(key)

@register.filter(name='round')
def rounded(value):
    return round(value)
