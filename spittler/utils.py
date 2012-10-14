# -*- coding: utf-8 -*-

import datetime
import imghdr
import os.path
import random
from untitled.settings import MEDIA_ROOT

def slug_generator():
    """ Function generates utility fields that will be used inside of the system """
    current_date = datetime.datetime.now()
    return u'%04d%02d%02d%02d%02d%02d%03d' % (
        current_date.year, current_date.month,
        current_date.day, current_date.hour,
        current_date.minute, current_date.second,
        random.randint(0, 999)
        )


def handle_uploaded_file(f, id):
    """ Handles uploaded file """
    if f is not None and is_valid_image(f):
        with open('%s/%s' % (MEDIA_ROOT, id), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def clean_up(id):
    """ Removes uploaded image bonded to spittle being deleted """
    file = '%s/%s' % (MEDIA_ROOT, id)
    if os.path.exists(file):
        os.unlink(file)


def is_valid_image(f):
    return imghdr.what(f) in ['png', 'gif', 'jpeg', 'bmp']
