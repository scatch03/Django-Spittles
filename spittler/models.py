# -*- coding: utf-8 -*-

from django.db import models
from spittler.utils import slug_generator

class Spittle(models.Model):
    '''
        Model class for representing simple message (i.e spittle)
    '''

    _text = models.TextField(null=False, default='')
    _slug = models.SlugField(db_index=True, unique=True, default=slug_generator)
    _subject = models.CharField(max_length=120, null=False, default=u'No Subject')
    _has_image = models.BooleanField(null=False, default=False)

    @property
    def image(self):
        return self._has_image

    @image.setter
    def image(self, value):
        self._has_image = value

    @property
    def message(self):
        return self._text

    @message.setter
    def message(self, value):
        self._text = value

    @property
    def identity(self):
        return self._slug

    @identity.setter
    def identity(self, value):
        self._slug = value

    def get_title(self):
        return self._subject

    def set_title(self, value):
        self._subject = value

    title = property(get_title, set_title)