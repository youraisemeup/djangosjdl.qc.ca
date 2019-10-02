from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from sjdl.careers.models import Careers

def index(request):
    careers = Careers.current_careers_list()
    return render(request, 'careers/index.html',{'careers':careers})

def detail(request, slug):
    careers = Careers.current_careers_list()
    job = get_object_or_404(Careers, slug=slug)

    return render(request, 'careers/detail.html', {'careers':careers,'job':job})