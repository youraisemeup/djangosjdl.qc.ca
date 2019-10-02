from django.conf.urls import patterns, url
from sjdl.careers import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>.*)/$', views.detail, name='detail')
)