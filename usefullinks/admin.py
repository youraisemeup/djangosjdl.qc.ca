#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from sjdl.usefullinks.models import UsefulLinks, RepertoryLinks

class UsefulLinksAdmin(admin.ModelAdmin):
    list_display = ("title","categorie")
    ordering = ['title']

class RepertoryLinksAdmin(admin.ModelAdmin):
    list_display = ("title","repertory_category","usefullink_category")
    ordering = ['-repertory_category','title']

admin.site.register(UsefulLinks,UsefulLinksAdmin)
admin.site.register(RepertoryLinks,RepertoryLinksAdmin)