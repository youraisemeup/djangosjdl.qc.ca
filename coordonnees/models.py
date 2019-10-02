#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from mezzanine.core.fields import RichTextField, MultiChoiceField, FileField
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page
from django.utils.functional import lazy


def getAvailablePages(self):
    return Page.objects.all().exclude(in_menus = '')

class Coordonnees(Orderable):
    contact_name = models.CharField(max_length=255, verbose_name='Nom du contact', blank=True, null=True)
    contact_title = models.CharField(max_length=255, verbose_name='Titre du contact', blank=True, null=True)
    telephone = models.CharField(max_length=255, verbose_name='Téléphone', blank=True, null=True)
    fax = models.CharField(max_length=255, verbose_name='Télécopieur', blank=True, null=True)
    email = models.EmailField(verbose_name='Courriel',blank=True,null=True)
    ik_image = FileField("Image", max_length=200, upload_to="", blank=True, null=True)
    address = RichTextField(verbose_name='Adresse', blank=True, null=True)
    pages = models.ManyToManyField(Page)

    def __unicode__(self):
        return self.contact_name

    def display_pages(self):
        return ', '.join([ pages.title for pages in self.pages.all() ])
    display_pages.short_description = 'Pages'

    search_fields = ['contact_name']
    ordering=['_order','contact_name']

    class Meta:
        verbose_name = 'Coordonnées'
        verbose_name_plural = 'Coordonnées'
