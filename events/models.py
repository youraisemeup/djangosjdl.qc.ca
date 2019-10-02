#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mezzanine.galleries.models import Gallery
import datetime
from mezzanine.core.fields import FileField
from mezzanine.core.models import RichText, Displayable

#@todo: conditional validation

class Events(Displayable, RichText):

    EVENT_CATEGORY_CHOICES = (
        (
            1,'Général'
        ),(
            2,'Collecte bac brun'
        ),(
            3,'Collecte bac bleu'
        ),(
            4,'Collecte ordures'
        ),(
            5,'Écocentre'
        )
    )

    ik_image = FileField("Image", max_length=200, upload_to="", blank=True, null=True)
    ik_diapo = models.ForeignKey("galleries.Gallery", verbose_name="Diaporama", blank=True, null=True, default=None)
    s_link = models.URLField(max_length=255, verbose_name='Lien externe', blank=True, null=True)
    s_link_title = models.CharField(max_length=255, verbose_name='Titre du lien', blank=True, null=True)
    s_link_youtube = models.URLField(max_length=255, verbose_name='Lien Youtube', blank=True, null=True)
    b_home = models.BooleanField(verbose_name="Afficher dans le slider de la page d'accueil", blank=True, default=False)
    ik_home_image = FileField("Image Slider", max_length=200, upload_to="", blank=True, null=True)
    s_excerpt_home = models.TextField(verbose_name='Resume 150 caracteres', max_length=150, blank=True, null=True)
    eventType = models.IntegerField(verbose_name='Type d\'événement', choices=EVENT_CATEGORY_CHOICES,default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('events:detail', kwargs={'slug':self.slug})

    search_fields = ['title']
    ordering=['-publish_date']

    class Meta:
        verbose_name = 'Événement'
        verbose_name_plural = 'Événements'


class EventDates(models.Model):
    event = models.ForeignKey(Events, to_field="id")
    dt_debut = models.DateField(verbose_name='Date de debut', default=None)
    dt_fin = models.DateField(verbose_name='Date de fin', blank=True, null=True)

    ordering = ['dt_debut']

    def __str__(self):
        return self.dt_debut.strftime('%Y-%m-%d')

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

    @staticmethod
    def next_event(category=1):
        return EventDates.objects.all().filter(
            event__eventType = category
        ).filter(
            dt_debut__gte = datetime.date.today()
        ).filter(
            event__status = 2
        ).distinct('event').order_by('event','dt_debut')[:1]

    @staticmethod
    def latest_events_list():
        events = EventDates.objects.extra(
            select={'class':"(case when dt_debut <= current_date then 'current' else '' end)",'date':"(case when dt_debut < current_date then current_date else dt_debut end)"}
        ).select_related('event').filter(
            event__publish_date__lte = datetime.datetime.now()
        ).filter(
            models.Q(dt_debut__gte = datetime.datetime.today()) | models.Q(models.Q(dt_fin__gte = datetime.datetime.today()) & models.Q(dt_debut__lte = datetime.datetime.today()))
        ).order_by('dt_debut')
        return events