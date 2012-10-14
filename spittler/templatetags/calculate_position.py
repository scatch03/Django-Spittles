# -*- coding: utf-8 -*-

from django.template.defaulttags import register
from spittler.settings.settings import Settings
import random

@register.filter(name='calculate_top')
def calculate_tag_position_vertically(value, delta):
    """ Calculates spittle top position in browser window """
    return random.randint(0, 50) + delta * (value % Settings.VERTICAL_SCALE)


@register.filter(name='calculate_left')
def calculate_tag_position_horizontally(value, delta):
    """ Calculates spittle left position in browser window """
    return random.randint(0, 25) + delta * (value / Settings.VERTICAL_SCALE)


@register.filter(name='calculate_head_left')
def calculate_head_horizontal(spittles, delta, front=True):
    """ Calculates left position of the end of message list in browser window """
    message_count = len(spittles)
    if not front:
        delta = 0
    return random.randint(0, 25) + delta * (message_count / Settings.VERTICAL_SCALE)


@register.filter(name='calculate_head_top')
def calculate_head_horizontal(spittles, delta, front=True):
    """ Calculates top position of the end of message list in browser window """
    message_count = len(spittles)
    if not front:
        delta = 0
    return random.randint(30, 50) + delta * (message_count % Settings.VERTICAL_SCALE)



