#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class CIForm(forms.Form):
    email = forms.EmailField(max_length=255, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Courriel'}))
    firstname = forms.CharField(max_length=255, label='Prénom',required=False, widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    lastname = forms.CharField(max_length=255, label='Nom',required=False, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
