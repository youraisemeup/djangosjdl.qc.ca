#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from django.contrib.sitemaps import FlatPageSitemap
from django.db.models import Min,Max
import datetime
from django.db.models import Q
from mezzanine.pages.models import Page
from itertools import chain
from operator import attrgetter
from sjdl.news.models import News
from sjdl.events.models import Events,EventDates
from sjdl.documentation.models import BulletinsMunicipaux
from sjdl.documentation.models import InfoLoisirs
from sjdl.infotravaux.models import InfoTravaux
from sjdl.common.forms import CoffretForm


def home(request):

    #get news and events to appear in the homepage slider
    slidernews = News.objects.extra(
        select={'date':'publish_date::date','type':"'news'",'truncatevalue':"18 - (length(title) - length(replace(title,' ',''))+1)"}
    ).filter(
        publish_date__lte = datetime.datetime.now()
    ).filter(
        Q(expiry_date__gte = datetime.datetime.now()) | Q(expiry_date__isnull = True)
    ).filter(
        b_home = True
    ).filter(
        status = 2
    ).order_by('publish_date')

    #we only want the first occurence of the object to appear in the slider, not all dates!
    sliderevents = Events.objects.extra(
        select={
            'date':'(select dt_debut from events_eventdates where events_events.id = events_eventdates.event_id and events_eventdates.dt_debut >= current_date order by events_eventdates.dt_debut limit 1)',
            'type':"'events'",
            'truncatevalue':"18 - (length(title) - length(replace(title,' ',''))+1)"
        }
    ).filter(
        b_home = True
    ).filter(
        eventdates__dt_debut__gte = datetime.date.today()
    ).distinct().order_by('date')

    result_list = chain(sliderevents,slidernews)
    sliderimages = sorted(result_list, key=attrgetter('date'))

    #get news that dont appear in slider
    recentnews = News.objects.filter(
        publish_date__lte = datetime.datetime.now()
    ).filter(
        Q(expiry_date__gte = datetime.datetime.now()) | Q(expiry_date__isnull = True)
    ).filter(
        Q(b_home__isnull = True) | Q(b_home = False)
    ).filter(
        status = 2
    ).order_by('-publish_date')[:3]

    recentevents = EventDates.latest_events_list().filter(
        Q(event__b_home__isnull = True) | Q(event__b_home = False)
    )[:8]

    #get most recent bulletin municipal (yes yes full frenglish)
    bulletin = BulletinsMunicipaux.mostRecent()
    #bulletin = InfoLoisirs.mostRecent()

    #get info travaux
    travaux = InfoTravaux.objects.filter(
        publish_date__lte = datetime.datetime.now()
    ).filter(
        Q(expiry_date__gte = datetime.datetime.now()) | Q(expiry_date__isnull = True)
    ).filter(
        status = 2
    ).order_by('-publish_date')


    return render(request, 'homepage.html', {'sliderimages':sliderimages, 'recentnews':recentnews, 'recentevents':recentevents, 'bulletin':bulletin, 'travaux':travaux})

def sitemap(request):

    menuitems = Page.objects.all().exclude(in_menus = '').order_by('_order')

    return render(request,'plan-du-site.html',{'menupages':menuitems})
    
def pg_elections(request):

    menuitems = Page.objects.all().exclude(in_menus = '').order_by('_order')

    return render(request,'elections.html',{'menupages':menuitems}) 

def coffretform(request):
    if request.method == 'POST':
        form = CoffretForm(request.POST)
        if form.is_valid():
            #print
            return
    else:
        form = CoffretForm()
    return render(request, 'common/form-coffret.html',{'form':form,'basePriceWithout':'90.00','basePriceWith':'105.00','basePriceShipping':'12.00'})

def coffretformprint(request):
    if request.method == 'POST':
        form = CoffretForm(request.POST)

        priceWithout = int(request.POST.get("iCountWithout")) * 90
        priceWith = int(request.POST.get("iCountWith")) * 105
        priceShipping = (int(request.POST.get("iCountWith")) + int(request.POST.get("iCountWithout"))) * 12
        total = priceWithout + priceWith + priceShipping
    else:
        return HttpResponseRedirect('formulaire-de-commande')
    return render(request, 'common/coffret-print.html',{'form':form,'priceWithout':format(priceWithout,'.2f'),'priceWith':format(priceWith,'.2f'),'priceShipping':format(priceShipping,'.2f'), 'total':format(total,'.2f')})
