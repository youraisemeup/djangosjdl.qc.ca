#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from sjdl.events.models import Events,EventDates
from mezzanine.galleries.models import Gallery
from mezzanine.galleries.models import GalleryImage

def listing(request):
    #events = Events.latest_events_list()
    events = EventDates.latest_events_list()
    sidebarevents = events[:8]
    return render(request, 'events/index.html', {'events':events,'sidebarevents':sidebarevents})

"""class IndexView(generic.ListView):
    template_name = 'events/index.html'

    def get_queryset(self):
        return Events.latest_events_list()"""


def detail(request, slug):
    #sidebarevents = Events.latest_events_list()[:8]
    sidebarevents = EventDates.latest_events_list()[:8]
    current_event = get_object_or_404(Events, slug=slug)
    images = None

    if current_event.ik_diapo_id is not None:
        gallery = Gallery.objects.get(id=news.ik_diapo_id)
        images = GalleryImage.objects.all().filter(gallery_id=gallery.id)

    return render(request, 'events/detail.html', {'sidebarevents':sidebarevents, 'current_event':current_event,'images':images})