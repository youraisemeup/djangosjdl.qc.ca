from django.contrib import admin
from sjdl.coordonnees.models import Coordonnees
from django.forms.models import ModelMultipleChoiceField
from mezzanine.pages.models import Page

class CoordonneesAdmin(admin.ModelAdmin):
    """def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pages":
            queryset = Page.objects.all().exclude(in_menus = '').order_by('_order')
            return ModelMultipleChoiceField(queryset)
        else:
            return super(CoordonneesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)"""

    list_display = ('contact_name','telephone','display_pages')
    ordering = ('_order','contact_name')

admin.site.register(Coordonnees,CoordonneesAdmin)