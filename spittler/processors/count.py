# -*- coding: utf-8 -*-

from spittler.models import Spittle

def spittles_count(request):
    return{
        'spittles_count': Spittle.objects.count()
    }
