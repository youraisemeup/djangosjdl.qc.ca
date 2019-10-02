from django.contrib import admin
from sjdl.faq.models import Faq

class FaqAdmin(admin.ModelAdmin):
    ordering = ('title',)

admin.site.register(Faq,FaqAdmin)