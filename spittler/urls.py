# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from untitled import settings

urlpatterns = patterns('',
    url(r'spittlers/$', 'spittler.views.list_spittlers'),
    url(r'add/$', 'spittler.views.add_spittle'),
    url(r'delete/([0-9]+)$', 'spittler.views.delete_spittle'),
    url(r'spittle/random$', 'spittler.views.random_spittle'),
    url(r'demo$', 'spittler.views.demo_widget'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

