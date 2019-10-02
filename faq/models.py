#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mezzanine.galleries.models import Gallery
import datetime
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Displayable

class Faq(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=200, default='')
    content = RichTextField(verbose_name='Texte')

    def __unicode__(self):
        return self.title

    search_fields = ['title']
    ordering=['title']

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
