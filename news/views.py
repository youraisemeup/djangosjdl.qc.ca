from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
import calendar
from django.db.models import Q
from sjdl.news.models import News
from mezzanine.galleries.models import Gallery
from mezzanine.galleries.models import GalleryImage

def listing(request):
    news = News.latest_news_list()[:8]

    archives = News.latest_news_list()

    return render(request, 'news/index.html', {'news':news,'archives':archives})

def archives(request, year, month):
    monthrange = calendar.monthrange(int(year), int(month))
    
    dateMin = datetime.date(int(year),int(month),1)
    dateMax = datetime.date(dateMin.year, dateMin.month, monthrange[1])

    news = News.objects.filter(
            Q(publish_date__range = (dateMin,dateMax)) | Q(publish_date__isnull = True)
        ).filter(
            Q(expiry_date__gte = dateMax) | Q(expiry_date__isnull = True)
        ).filter(
            status = 2
        ).order_by('-publish_date')

    archives = News.latest_news_list()

    return render(request, 'news/index.html', {'news':news,'archives':archives})

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    images = None

    if news.ik_diapo_id is not None:
        gallery = Gallery.objects.get(id=news.ik_diapo_id)
        images = GalleryImage.objects.all().filter(gallery_id=gallery.id)

    archives = News.latest_news_list()

    return render(request, 'news/detail.html', {'news':news, 'images':images,'archives':archives})