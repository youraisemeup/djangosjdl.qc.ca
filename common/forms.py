#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class CoffretForm(forms.Form):
    firstname = forms.CharField(max_length=255, label=u'Prénom', widget=forms.TextInput(attrs={'placeholder': u'Prénom'}))
    lastname = forms.CharField(max_length=255, label='Nom', widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    phone = forms.CharField(max_length=255, label=u'Téléphone', widget=forms.TextInput(attrs={'placeholder': u'Téléphone'}))
    email = forms.EmailField(max_length=255, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Courriel'}))

    ONE_TO_TEN_CHOICES = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )

    iCountWithout = forms.ChoiceField(label=u'Quantité', choices=ONE_TO_TEN_CHOICES, widget=forms.Select(attrs={'placeholder': u'Quantité'}))
    iCountWith = forms.ChoiceField(label=u'Quantité', choices=ONE_TO_TEN_CHOICES, widget=forms.Select(attrs={'placeholder': u'Quantité'}))
