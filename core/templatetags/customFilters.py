from django import template

import math

register = template.Library()


@register.filter(name="split")
def split(value, key):
    value.split(f"{key}")
    return value.split(key)


@register.filter(name="round")
def rounded(value):
    if int(value * 10) % 10 >= 5:
        return math.ceil(value)

    return math.floor(value)
