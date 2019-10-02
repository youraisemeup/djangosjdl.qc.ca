from django.contrib import admin
from sjdl.searchbac.models import BacBrun, BacBleu, Poubelle,Ecocentre,Grenier,Comite,Joujou,Arbres,Medicaments,Constantin

class BacBrunAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class BacBleuAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class PoubelleAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class EcocentreAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class GrenierAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class ComiteAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class JoujouAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class ArbresAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class MedicamentsAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False

class ConstantinAdmin(admin.ModelAdmin):
    ordering = ('keyword',)
    def in_menu(self):
        return False


#admin.site.register(SearchBac,SearchBacAdmin)
admin.site.register(BacBrun,BacBrunAdmin)
admin.site.register(BacBleu,BacBleuAdmin)
admin.site.register(Poubelle,PoubelleAdmin)
admin.site.register(Ecocentre,EcocentreAdmin)
admin.site.register(Grenier,GrenierAdmin)
admin.site.register(Comite,ComiteAdmin)
admin.site.register(Joujou,JoujouAdmin)
admin.site.register(Arbres,ArbresAdmin)
admin.site.register(Medicaments,MedicamentsAdmin)
admin.site.register(Constantin,ConstantinAdmin)