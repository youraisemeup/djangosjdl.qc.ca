#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
import datetime,re
from django.db.models import Q
from mezzanine.pages.models import Page
from itertools import chain
from operator import attrgetter
from sjdl.documentation.models import ProcesVerbauxConseil,InformationsFinancieres,ReglementsMunicipaux,ProcesVerbauxRegieTraitement,ProcesVerbauxRegieAssainissement,BulletinsMunicipaux,CalendriersMunicipaux,CommuniquesPresse,AvisPublics,InfoLoisirs

# Create your views here.
def conseilMunicipal(request):
    archives = ProcesVerbauxConseil.archives
    pageinfos = {'title':'Procès-verbaux','slug':'seances-du-conseil','path':request.path}
    return render(request, 'documentation/sidebar.html',{'archives':archives,'pageinfos':pageinfos})

def seancesConseilMunicipal(request, year = datetime.date.today().year):
    regex = re.compile('seances-du-conseil/$')
    if regex.search(request.path):
        relativepath = './'
    else:
        relativepath = '../'
    documents = ProcesVerbauxConseil.objects.all().filter(
        publish_date__year = year
    ).filter(
        publish_date__lte = datetime.datetime.now()
    ).order_by('-publish_date')
    archives = ProcesVerbauxConseil.archives
    pageinfos = {'metatitle':'Procès-verbaux','metadesc':'Procès-verbaux municipal','h1title':'Procès-verbaux','slug':'seances-du-conseil','relativepath':relativepath}
    return render(request, 'documentation/year.html', {'documents':documents, 'pageinfos':pageinfos,'archives':archives})

def ProcesVerbauxRegieAssainissementSeances(request):
    etatsfinanciers = ProcesVerbauxRegieAssainissement.archives(2)
    seances = ProcesVerbauxRegieAssainissement.archives(1)

    pageinfos = {'title':'Procès-verbaux','slug':'seances-et-proces-verbaux','path':'/services-municipaux/hygiene-du-milieu/regie-dassainissement-des-eaux-usees-de-deux-montagnes/'}
    return render(request, 'documentation/regies-sidebar.html',{'etatsfinanciers':etatsfinanciers,'seances':seances,'pageinfos':pageinfos})

def archivesPV_RA(request,year = datetime.date.today().year):
    etatsfinanciers = ProcesVerbauxRegieAssainissement.archives(2)
    seances = ProcesVerbauxRegieAssainissement.archives(1)

    documents = seances.filter(publish_date__year = year).order_by('-publish_date')
    pageinfos = {'metatitle':'Procès-verbaux','metadesc':'Procès-verbaux de la Régie d\'assainissement des eaux usées de Deux-Montagnes','h1title':'Procès-verbaux','slug':'seances-et-proces-verbaux'}
    return render(request, 'documentation/regies.html', {'documents':documents,'pageinfos':pageinfos,'etatsfinanciers':etatsfinanciers,'seances':seances})

def ProcesVerbauxRegieTraitementSeances(request):
    etatsfinanciers = ProcesVerbauxRegieTraitement.archives(2)
    seances = ProcesVerbauxRegieTraitement.archives(1)

    pageinfos = {'title':'États financiers','slug':'seances-et-proces-verbaux','path':'/services-municipaux/hygiene-du-milieu/regie-de-traitement-des-eaux-usees-de-deux-montagnes/'}
    return render(request, 'documentation/regies-sidebar.html',{'etatsfinanciers':etatsfinanciers,'seances':seances,'pageinfos':pageinfos})

def archivesPV_RT(request,year = datetime.date.today().year):
    etatsfinanciers = ProcesVerbauxRegieTraitement.archives(2)
    seances = ProcesVerbauxRegieTraitement.archives(1)

    documents = seances.filter(publish_date__year = year).order_by('-publish_date')
    pageinfos = {'metatitle':'Procès-verbaux','metadesc':'Procès-verbaux de la Régie de traitement des eaux usées de Deux-Montagnes','h1title':'Procès-verbaux','slug':'proces-verbaux'}
    return render(request, 'documentation/regies.html', {'documents':documents, 'pageinfos':pageinfos,'etatsfinanciers':etatsfinanciers,'seances':seances})

def informationsFinancieres(request):
    documents = InformationsFinancieres.objects.all().filter(
        publish_date__lte = datetime.datetime.now()
    ).order_by('-publish_date')
    pageinfos = {'metatitle':'Informations financières','metadesc':'Informations financières','h1title':'Informations financières'}
    return render(request, 'documentation/categories.html', {'documents':documents, 'pageinfos':pageinfos})

def reglementsMunicipaux(request):
    documents = ReglementsMunicipaux.objects.all().filter(
        publish_date__lte = datetime.datetime.now()
    ).order_by('title')
    pageinfos = {'metatitle':'Règlements municipaux','metadesc':'Règlements municipaux de Saint-Joseph-du-Lac','h1title':'Règlements municipaux'}

    return render(request, 'documentation/reglementsmunicipaux.html',{'categories':documents, 'pageinfos':pageinfos})

def publications(request, year=datetime.date.today().year):
    #bulletins municipaux, calendriers, communiqués de presse, avis publics
    bulletins = BulletinsMunicipaux.objects.all().filter(publish_date__year = year).order_by('-publish_date')
    loisirs = InfoLoisirs.objects.all().filter(publish_date__year = year).order_by('-publish_date')
    calendriers = CalendriersMunicipaux.objects.all().filter(publish_date__year = year).order_by('-publish_date')
    communiques = CommuniquesPresse.objects.all().filter(publish_date__year = year).order_by('-publish_date')

    documents = chain(BulletinsMunicipaux.archives(), InfoLoisirs.archives(), CalendriersMunicipaux.archives(), CommuniquesPresse.archives())

    documents = sorted(documents, key=attrgetter('publish_date'), reverse=True)

    pageinfos = {'metatitle':'Publications','metadesc':'Publications de la municipalité de Saint-Joseph-du-Lac','h1title':'Publications','slug':'publications'}
    return render(request, 'documentation/publications.html', {'currentyear':year, 'documents':documents, 'bulletins':bulletins, 'loisirs':loisirs, 'calendriers':calendriers, 'communiques':communiques, 'pageinfos':pageinfos})

def avispublics(request, year = datetime.date.today().year):
    regex = re.compile('avis-publics/$')
    if regex.search(request.path):
        relativepath = './'
    else:
        relativepath = '../'

    documents = AvisPublics.objects.all().filter(
        publish_date__year = year
    ).filter(
        publish_date__lte = datetime.datetime.now()
    ).filter(
        Q(end_date__gte = datetime.datetime.now()) | Q(end_date__isnull = True)
    ).order_by('-publish_date')

    archives = AvisPublics.archives
    pageinfos = {'slug':'avis-publics','relativepath':relativepath,'showpage':True}
    return render(request, 'documentation/avis-publics.html', {'documents':documents, 'pageinfos':pageinfos,'archives':archives})