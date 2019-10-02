#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from sjdl.documentation.models import ProcesVerbauxConseil, ProcesVerbauxRegieAssainissement, ProcesVerbauxRegieTraitement, PolitiquesEnvironnementales, ReglementsMunicipaux,DocumentReglementsMunicipaux, InformationsFinancieres, BulletinsMunicipaux, CalendriersMunicipaux, CommuniquesPresse, AvisPublics, InfoLoisirs
from sjdl.common.models import DocumentPage, DocumentPageDocument

class DocumentReglementsMunicipauxInline(TabularDynamicInlineAdmin):
    model = DocumentReglementsMunicipaux

class ReglementsMunicipauxAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ['title']
    ordering = ['title']
    inlines = (DocumentReglementsMunicipauxInline,)

class ProcesVerbauxConseilAdmin(admin.ModelAdmin):
    list_display = ("title","publish_date")

class ProcesVerbauxRegieAssainissementAdmin(admin.ModelAdmin):
    list_display = ("title",'category',"publish_date")
    ordering = ['-category','-publish_date']

class ProcesVerbauxRegieTraitementAdmin(admin.ModelAdmin):
    list_display = ("title",'category',"publish_date")
    ordering = ['-category','-publish_date']

admin.site.register(ProcesVerbauxConseil,ProcesVerbauxConseilAdmin)
admin.site.register(ProcesVerbauxRegieAssainissement,ProcesVerbauxRegieAssainissementAdmin)
admin.site.register(ProcesVerbauxRegieTraitement,ProcesVerbauxRegieTraitementAdmin)
#admin.site.register(PolitiquesEnvironnementales)
admin.site.register(ReglementsMunicipaux,ReglementsMunicipauxAdmin)
#admin.site.register(InformationsFinancieres)
admin.site.register(BulletinsMunicipaux)
admin.site.register(InfoLoisirs)
admin.site.register(CalendriersMunicipaux)
admin.site.register(CommuniquesPresse)
admin.site.register(AvisPublics)

class DocumentPageDocumentInline(TabularDynamicInlineAdmin):
    model = DocumentPageDocument

class DocumentPageAdmin(PageAdmin):
    inlines = (DocumentPageDocumentInline,)

admin.site.register(DocumentPage,DocumentPageAdmin)