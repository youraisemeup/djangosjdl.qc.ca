from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.db.models import Q
from sjdl.infotravaux.models import InfoTravaux
from mezzanine.galleries.models import Gallery
from mezzanine.galleries.models import GalleryImage

def listing(request):
    infotravaux = InfoTravaux.latest_infos_list()

    current_list = InfoTravaux.latest_infos_list()

    return render(request, 'infotravaux/index.html', {'infotravaux':infotravaux})

"""class IndexView(generic.ListView):
    template_name = 'infotravaux/index.html'

    def get_queryset(self):
        return InfoTravaux.latest_infos_list()"""


def detail(request, slug):
    infotravaux = InfoTravaux.latest_infos_list()
    current_chantier = get_object_or_404(InfoTravaux, slug=slug)

    images = None
    if current_chantier.ik_diapo_id is not None:
        gallery = Gallery.objects.get(id=news.ik_diapo_id)
        images = GalleryImage.objects.all().filter(gallery_id=gallery.id)

    return render(request, 'infotravaux/detail.html', {'infotravaux':infotravaux, 'current_chantier':current_chantier, 'images':images})