#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mezzanine.galleries.models import Gallery
import datetime
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Orderable, RichText
from django.db.models import Q
from django import forms
from django.template.defaultfilters import slugify

class BaseDocument(models.Model):
    #categorie = models.ForeignKey("Category", related_name="document")
    file = FileField("Document", max_length=200, format="Document", upload_to="documents", extensions=[".pdf"])
    title = models.CharField(verbose_name = "Titre",max_length=200, default="")
    publish_date = models.DateTimeField("Date de publication",default=datetime.datetime.now)

    search_fields = ['title']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

#Séances et procès-verbaux – Conseil municipal : Par année
class ProcesVerbauxConseil(BaseDocument):

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = ProcesVerbauxConseil.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = 'Séances et procès-verbaux – Conseil municipal'

#Séances et procès-verbaux – Régie assainisement des eaux
class ProcesVerbauxRegieAssainissement(BaseDocument):

    category = models.IntegerField(verbose_name="Catégorie", default=1, choices=((1,"Séances et procès verbaux"),(2,"États financiers")))

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives(categoryid):
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = ProcesVerbauxRegieAssainissement.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).filter(
            category = categoryid
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = 'Régie assainisement des eaux'

#Séances et procès-verbaux – Régie de traitement des eaux usées
class ProcesVerbauxRegieTraitement(BaseDocument):
    category = models.IntegerField(verbose_name="Catégorie", default=1, choices=((1,"Séances et procès verbaux"),(2,"États financiers")))

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives(categoryid):
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = ProcesVerbauxRegieTraitement.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).filter(
            category = categoryid
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = 'Régie de traitement des eaux usées'

#Politiques environnementale et règlements municipaux : Présentation par catégories
class PolitiquesEnvironnementales(BaseDocument):

    def __unicode__(self):
        return self.title

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Politiques environnementales'

class ReglementsMunicipaux(Displayable,RichText):
    #title = models.CharField(verbose_name = "Titre",max_length=200, default="")
    #publish_date = models.DateTimeField("Date de publication",default=datetime.datetime.now)
    #text = RichTextField(verbose_name='Texte')

    search_fields = ['title','content']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('regmunicipaux', kwargs={})

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Règlements municipaux'

class DocumentReglementsMunicipaux(models.Model):
    reglement = models.ForeignKey("ReglementsMunicipaux", related_name="documents")
    doctitle = models.CharField(verbose_name = "Titre du document",max_length=200, default="")
    file = FileField("Document", max_length=200, format="Document", upload_to="documents", extensions=[".pdf"])

    search_fields = ['title']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __unicode__(self):
        return self.doctitle

#Informations financières - Présentation par catégories
class InformationsFinancieres(BaseDocument):
    categorie = models.IntegerField(verbose_name="Catégorie", default=1, choices=((1,"Catégorie 1"),(2,"Catégorie 2")))

    def __unicode__(self):
        return self.title

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Informations financières'

#Bulletins municipaux
class BulletinsMunicipaux(BaseDocument):
    image = FileField("Image", max_length=200, upload_to="bulletins", blank=True, null=True)
    titleloisirs = models.CharField(verbose_name = "Titre PDF Loisirs",max_length=200, default="", null=True, blank=True)
    docloisirs = FileField("Document Loisirs", max_length=200, format="Document", upload_to="documents", extensions=[".pdf"], null=True, blank=True)
    imageloisirs = FileField("Image Loisirs", max_length=200, upload_to="bulletins", blank=True, null=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def mostRecent():
        return BulletinsMunicipaux.objects.all().order_by('-publish_date')[:1]

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = BulletinsMunicipaux.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Bulletins municipaux'

#Calendriers municipaux
class CalendriersMunicipaux(BaseDocument):

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = CalendriersMunicipaux.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Calendriers municipaux'

#Communiqués de presse
class CommuniquesPresse(BaseDocument):

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = CommuniquesPresse.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Communiqués de presse'

#Avis Publics
class AvisPublics(BaseDocument):
    end_date = models.DateTimeField("Date de fin d'affichage",blank=True,null=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = AvisPublics.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).filter(
            Q(end_date__gte = datetime.datetime.now()) | Q(end_date__isnull = True)
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Avis publics'

#Info Loisirs
class InfoLoisirs(BaseDocument):
    image = FileField("Image", max_length=200, upload_to="loisirs", blank=True, null=True)
    titleloisirs = models.CharField(verbose_name = "Titre PDF Loisirs",max_length=200, default="", null=True, blank=True)
    docloisirs = FileField("Document Loisirs", max_length=200, format="Document", upload_to="documents", extensions=[".pdf"], null=True, blank=True)
    imageloisirs = FileField("Image Loisirs", max_length=200, upload_to="loisirs", blank=True, null=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def mostRecent():
        return InfoLoisirs.objects.all().order_by('-publish_date')[:1]

    @staticmethod
    def archives():
        startdate = datetime.date(datetime.date.today().year -2,01,01)
        enddate = datetime.date(datetime.date.today().year,12,31)
        archives = InfoLoisirs.objects.all().filter(
            publish_date__range = [startdate,enddate]
        ).order_by('-publish_date')
        return archives

    search_fields = ['title']
    admin_order = ['-publish_date']

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Info Loisirs'