#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

class SearchBacForm(forms.Form):
    keyword = forms.CharField(max_length=255, required=True, label=u'Mot-clé', widget=forms.TextInput(attrs={'placeholder':u'Mot-clé'}))