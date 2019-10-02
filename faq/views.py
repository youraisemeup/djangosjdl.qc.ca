from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from sjdl.faq.models import Faq

def listing(request):
    faqitems = Faq.objects.all().order_by('title')
    return render(request, 'faq/index.html', {'faqitems':faqitems})