# -*- coding: utf-8 -*-

from django import forms

class AddSpittleForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 16, 'rows': 5, 'style': 'resize:none;'}))
    file = forms.FileField(label='', required=False)
