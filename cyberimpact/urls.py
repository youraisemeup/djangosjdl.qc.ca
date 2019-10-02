from django.conf.urls import patterns, url
from sjdl.cyberimpact import views

urlpatterns = patterns('',
    url(r'^inscription$', views.subscribe, name='inscription'),
    url(r'^succes$', views.succes, name='succes'),
    url(r'^erreur$', views.erreur, name='erreur'),
    url(r'^confirmation', views.confirmation, name='confirmation'),
)