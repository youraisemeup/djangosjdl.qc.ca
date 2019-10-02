from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from sjdl.searchbac.models import BacBrun,BacBleu,Poubelle,Ecocentre,Grenier,Comite,Joujou,Arbres,Medicaments,Constantin
from sjdl.searchbac.forms import SearchBacForm
from sjdl.events.models import Events,EventDates
import re
from django.template import RequestContext, loader

def search(request):
    results = False
    keyword = None
    context = RequestContext(request)
    if request.method == 'POST':
        form = SearchBacForm(request.POST)
        if form.is_valid():
            keyword = request.POST.get("keyword")

            bacbrun = BacBrun.objects.search(keyword)
            bacbleu = BacBleu.objects.search(keyword)
            poubelle = Poubelle.objects.search(keyword)
            ecocentre = Ecocentre.objects.search(keyword)
            grenier = Grenier.objects.search(keyword)
            comite = Comite.objects.search(keyword)
            joujou = Joujou.objects.search(keyword)
            arbres = Arbres.objects.search(keyword)
            medicaments = Medicaments.objects.search(keyword)
            constantin = Constantin.objects.search(keyword)

            if bacbrun or bacbleu or poubelle or ecocentre or grenier or comite or joujou or arbres or medicaments or constantin:
                results = True

            nextevent_bacbrun = EventDates.next_event(2)

            nextevent_bacbleu = EventDates.next_event(3)

            nextevent_poubelle = EventDates.next_event(4)

            nextevent_ecocentre = EventDates.next_event(5)

            context = RequestContext(request,{'bacbrun':bacbrun,'bacbleu':bacbleu,'poubelle':poubelle,'ecocentre':ecocentre,'grenier':grenier,'comite':comite,'joujou':joujou,'arbres':arbres,'medicaments':medicaments,'constantin':constantin,'keyword':keyword,'results':results,'nextevent_bacbrun':nextevent_bacbrun,'nextevent_bacbleu':nextevent_bacbleu,'nextevent_poubelle':nextevent_poubelle,'nextevent_ecocentre':nextevent_ecocentre})
    else:
        form = SearchBacForm()
    t = loader.get_template('searchbac/index.html')
    #context = RequestContext(request,{'bacbrun':bacbrun,'bacbleu':bacbleu,'bacvert':bacvert,'keyword':keyword})
    return HttpResponse(t.render(context))