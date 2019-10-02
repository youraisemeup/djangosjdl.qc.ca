from django.conf.urls import patterns, url
from sjdl.common import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)