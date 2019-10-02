from django.conf.urls import patterns, url
from sjdl.news import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.listing, name='index'),
    url(r'^(\d{4})/(\d{2})/$', views.archives, name='archives'),
    url(r'^(?P<slug>.*)/$', views.detail, name='detail')
)