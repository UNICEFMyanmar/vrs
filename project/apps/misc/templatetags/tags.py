# -*- coding: utf-8 -*-
import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.defaultfilters import stringfilter
from django.utils import translation
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return ' class ="active" '
    return ''


@register.simple_tag
def reverse_active(request, url, return_value):
    """class="top-menu-element{% reverse_active request "frontpage.views" %}"""
    if reverse(url) == request.path:
        return return_value
    return ""


@register.filter(name='display')
def display_value(bound_field):
    field = bound_field.field
    if hasattr(field, 'choices'):
        flat = []
        for choice, value in field.choices:
            if isinstance(value, (list, tuple)):
                flat.extend(value)
            else:
                flat.append((choice,value))
        return dict(flat).get(bound_field.data, bound_field.data)
    else:
        return bound_field.data

def convert_num_to_mm(value):
    if value:
        intab = u"0123456789"
        outtab = u"၀၁၂၃၄၅၆၇၈၉"
        intab = [ord(char) for char in intab]
        translate_table = dict(zip(intab, outtab))
        return unicode(value).translate(translate_table)
    else:
        return value


@register.filter
def num_to_mm(value):  # convert english numerals into myanmar numerals
    if translation.get_language() == "my":
        return convert_num_to_mm(value)
    else:
        return value


@register.filter(name='strip_before_delimiter')
def strip_before_delimiter(value):
    if not value:
        return ""
    value = unicode(value)
    if value:
        delimiter = "-"
        if delimiter in value:
            return value.split(delimiter, 1)[1]
        else:
            return value
    else:
        return ""


@register.filter(name='name')
def form_model_meta_model_name(form):
    """
    :param form
    :return: form model name
    Usage: {% form_model_meta_model_name form %}
    """
    return form.Meta.model._meta.model_name[1:]

@register.filter(is_safe=True)
@stringfilter
def ljust_n(value, arg=12):
    """
    Left-aligns the value in a field of a given width.

    Argument: field size.
    """
    return mark_safe("<u>" + value.ljust(int(arg), u"\u00A0") + "</u>")
