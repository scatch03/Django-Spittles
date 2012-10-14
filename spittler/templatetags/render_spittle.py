# -*- coding: utf-8 -*-

from spittler.models import Spittle
from django import template

register = template.Library()

def render_spittle_by_slug(slug_field, index):
    spittle = Spittle.objects.filter(slug=slug_field)
    return {'spittle': spittle, 'index': index}


def render_spittle(spittle, index):
    return {'spittle': spittle, 'index': index}

register.inclusion_tag('render_spittle.html')(render_spittle_by_slug)
register.inclusion_tag('render_spittle.html')(render_spittle)