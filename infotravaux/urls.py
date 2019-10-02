from django.conf.urls import patterns, url
from sjdl.infotravaux import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.listing, name='index'),
    url(r'^(?P<slug>.*)/$', views.detail, name='detail')
)