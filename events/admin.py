#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from sjdl.events.models import Events,EventDates
from mezzanine.core.admin import StackedDynamicInlineAdmin, TabularDynamicInlineAdmin

class EventDatesInline(TabularDynamicInlineAdmin):
    model = EventDates
    verbose_name = 'Date'
    verbose_name_plural = 'Dates'

class EventsAdmin(admin.ModelAdmin):
    EMPTY_DATE_SYMBOL = "-"
    list_display = ('get_first_date','title','eventType','b_home','status')
    #ordering = ('get_first_date','title')
    inlines = (EventDatesInline,)

    def get_first_date(self, obj):
        if obj.eventdates_set.count() == 0:
            return self.EMPTY_DATE_SYMBOL

        firstDay = obj.eventdates_set.all().order_by('dt_debut')[0]
        return firstDay.dt_debut

    get_first_date.short_description = 'Première occurence'

admin.site.register(Events,EventsAdmin)