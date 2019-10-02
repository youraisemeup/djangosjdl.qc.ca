#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from mezzanine.utils.views import paginate
from sjdl.usefullinks.models import UsefulLinks,RepertoryLinks,BaseLinks
import locale

def Agrotourisme(request, category):
    title = "Producteurs d'ici"
    links = RepertoryLinks.get_list(4)
    links = paginate(links, request.GET.get("page", 1),
                          8,#maxperpage
                          5)#maxpagination
    return render(request, 'usefullinks/producteurs.html', {'links':links,'title':title})

def fiche(request,category,slug):
    fiche = get_object_or_404(RepertoryLinks, slug=slug)
    return render(request, 'usefullinks/fiche.html', {'fiche':fiche})

def Organismes(request, category):
    title = "Organismes de la région"
    links = RepertoryLinks.get_list(1)
    return render(request, 'usefullinks/index.html', {'links':links,'title':title})

def OrganismesSportifs(request, category):
    title = "Organismes sportifs et de plein air"
    links = RepertoryLinks.get_list(2)
    return render(request, 'usefullinks/index.html', {'links':links,'title':title})

def Testo(request):
    val1 = str(locale.getlocale())
    val2 = str(locale.getdefaultlocale())
    val3 = val1 + val2
    return HttpResponse(val3)