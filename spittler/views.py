# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from spittler.forms.spittle import AddSpittleForm
from spittler.models import Spittle
from spittler.utils import handle_uploaded_file, clean_up, is_valid_image

def list_spittlers(request):
    """ Lists all current spittles on page """
    spittlers = Spittle.objects.all()
    form = AddSpittleForm()
    return render_to_response('spittlers.html', RequestContext(request, locals()))


def delete_spittle(request, id):
    """ Deletes spittle with given slug field """
    if request.method == 'POST':
        Spittle.objects.get(_slug=id).delete()
        clean_up(id)
    return HttpResponse()


def add_spittle(request):
    """ Adds spittle to current list """
    if request.method == 'POST':
        form = AddSpittleForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            spittle = Spittle()
            spittle.message = form.cleaned_data['message']
            spittle.title = form.cleaned_data['subject']
            if file is not None and is_valid_image(file):
                spittle.image = True
            Spittle.save(spittle)
            handle_uploaded_file(file, spittle.identity)

    return HttpResponseRedirect('/spittler/spittlers')


def random_spittle(request):
    """ Plucks random spittle """
    spittle = Spittle.objects.order_by('?')[0]
    return render_to_response('dynamic.html', RequestContext(request, locals()))


def demo_widget(request):
    """ Random spittle showing widget demo view """
    return render_to_response('widget.html', RequestContext(request, locals()))



