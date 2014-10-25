# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.assignment_tag
def class_lower(obj):
    try:
        return obj.__class__.__name__.lower()
    except AttributeError:
        return obj.__name__.lower()
