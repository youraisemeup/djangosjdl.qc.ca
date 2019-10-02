from django.conf.urls import patterns, url
from sjdl.animaux import views

urlpatterns = patterns('',
     url(r'^services-municipaux/gestion-animaliere/declaration-denregistrement-dun-chien/$', views.EnregistrementChienFormView.as_view(),
         name='enregistrementchienform'),
 )