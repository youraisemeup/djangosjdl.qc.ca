#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Displayable
from mezzanine.core.managers import SearchableManager

class SearchBac(models.Model):
    title = models.CharField(verbose_name='Nom du bac', max_length=200, default='')
    content = models.TextField(verbose_name='Mots clés')

    def __unicode__(self):
        return self.title

class BaseBac(models.Model):
    keyword = models.CharField(verbose_name='Mot clé', max_length=200, default='')
    content = RichTextField(verbose_name='Informations supplémentaires')

    def __unicode__(self):
        return self.title

    objects = SearchableManager()

    search_fields = ('keyword',)
    ordering=['keyword']

    class Meta:
        verbose_name = 'Mot-clé'
        verbose_name_plural = 'Mots-clé'

class BacBrun(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Bac Brun'
        verbose_name_plural = 'Mots-clé Bac Brun'

class BacBleu(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Bac Bleu'
        verbose_name_plural = 'Mots-clé Bac Bleu'

class Poubelle(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Poubelle'
        verbose_name_plural = 'Mots-clé Poubelle'

class Ecocentre(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Écocentre'
        verbose_name_plural = 'Mots-clé Écocentre'

class Grenier(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Grenier'
        verbose_name_plural = 'Mots-clé Grenier'

class Comite(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Comité d\'action sociale'
        verbose_name_plural = 'Mots-clé Comité d\'action sociale'

class Joujou(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Joujou RécupR'
        verbose_name_plural = 'Mots-clé Joujou RécupR'

class Arbres(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Arbres de Noël'
        verbose_name_plural = 'Mots-clé Arbres de Noël'

class Medicaments(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Médicaments'
        verbose_name_plural = 'Mots-clé Médicaments'

class Constantin(BaseBac):
    objects = SearchableManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Mot-clé Constantin'
        verbose_name_plural = 'Mots-clé Constantin'