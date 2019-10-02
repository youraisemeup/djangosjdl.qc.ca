#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from mezzanine.core.models import RichTextField, Displayable
from mezzanine.core.fields import FileField

class BaseLinks(Displayable):
    #linktitle = models.CharField(verbose_name="Titre", max_length=200, default="Titre")
    website = models.CharField(verbose_name="URL du lien", max_length=200, null=True, blank=True)

    search_fields = ['title']

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class UsefulLinks(BaseLinks):
    categorie = models.IntegerField(verbose_name="Catégorie", default=3, choices=((1,"Je Veux"),(2,"Liens rapides"),(3,"Liens utiles")))

    class Meta:
        verbose_name = 'Lien utile'
        verbose_name_plural = 'Liens utiles'

class RepertoryLinks(BaseLinks):
    excerpt = RichTextField(verbose_name="Bref résumé des services offerts ou de la mission de l'organisation",null=True,blank=True)
    address = models.CharField(verbose_name="Adresse", max_length=200, null=True, blank=True)
    city = models.CharField(verbose_name="Ville", max_length=200, null=True, blank=True)
    zipcode = models.CharField(verbose_name="Code Postal", max_length=200, null=True, blank=True)
    telephone = models.CharField(verbose_name="Téléphone", max_length=200, null=True, blank=True)
    fax = models.CharField(verbose_name="Télécopieur", max_length=200, null=True, blank=True)
    contactname = models.CharField(verbose_name="Personne ressource", max_length=200, null=True, blank=True)
    email = models.EmailField(verbose_name="Courriel",max_length=254,null=True,blank=True)
    ik_image = FileField("Image", max_length=200, upload_to="", blank=True, null=True)
    repertory_category = models.IntegerField(verbose_name="Catégorie de Répertoire", default=1, choices=((1,"Répertoire des organismes"),(2,"Répertoire des organismes sportifs"),(4,"Agrotourisme")))
    usefullink_category = models.IntegerField(verbose_name="Afficher dans les Liens utiles", null=True, blank=True, default=None, choices=((None,"---"),(1,"Je Veux"),(2,"Liens rapides"),(3,"Liens utiles")))

    @staticmethod
    def get_list(cat):
        return RepertoryLinks.objects.filter(
            publish_date__lte = datetime.datetime.now()
        ).filter(
            models.Q(expiry_date__gte = datetime.datetime.now()) | models.Q(expiry_date__isnull = True)
        ).filter(
            status = 2
        ).filter(
            repertory_category = cat
        ).order_by('title')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        if self.repertory_category == 1:
            category = 'organismes'
        elif self.repertory_category == 2:
            category = 'organismes-sportifs-et-de-plein-air'
        else:
            category = 'producteurs'

        if self.repertory_category == 4:
            return reverse('organismes', kwargs={'category':category,'slug':self.slug})
        else:
            return reverse('organismes', kwargs={'category':category})

    class Meta:
        verbose_name = 'lien'
        verbose_name_plural = 'liens du répertoire'


