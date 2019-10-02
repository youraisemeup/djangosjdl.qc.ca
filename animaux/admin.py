#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from sjdl.animaux.models import EnregistrementChien
from mezzanine.pages.models import Page
from import_export.admin import ExportMixin

class EnregistrementChienAdmin(ExportMixin, admin.ModelAdmin):

    list_display = ('id','get_proprietaire','created_at')
    ordering = ('-created_at','proprietaire_nom','proprietaire_prenom')

    fieldsets = (
        ("Propriétaire de l'animal", {
            "fields": (
                ("proprietaire_prenom", "proprietaire_nom"),
                ("proprietaire_telephone", "proprietaire_telephone_secondaire"),
                "proprietaire_courriel",
                ("proprietaire_adresse_no_civique", "proprietaire_adresse_rue", "proprietaire_adresse_app", "proprietaire_adresse_code_postal")
            )
        }),
        ("Identification du chien", {
            "fields": (
                "chien_nom",
                "chien_sexe",
                "chien_sterilise",
                "chien_age",
                "chien_race1",
                "chien_race1_autre",
                "chien_race2",
                "chien_race2_autre",
                "chien_couleur1",
                "chien_couleur2",
                "chien_micropuce",
                "chien_marques"
            )
        }),
        ("Stérilisation du chien", {
            "fields": (
                "chien_sterilisation_clinique_nom",
                "chien_sterilisation_clinique_adresse",
                "chien_sterilisation_clinique_telephone"
            )
        }),
        ("Identification du second chien", {
            "fields": (
                "chien2_nom",
                "chien2_sexe",
                "chien2_sterilise",
                "chien2_age",
                "chien2_race1",
                "chien2_race1_autre",
                "chien2_race2",
                "chien2_race2_autre",
                "chien2_couleur1",
                "chien2_couleur2",
                "chien2_micropuce",
                "chien2_marques"
            )
        }),
        ("Stérilisation du second chien", {
            "fields": (
                "chien2_sterilisation_clinique_nom",
                "chien2_sterilisation_clinique_adresse",
                "chien2_sterilisation_clinique_telephone"
            )
        }),
    )

admin.site.register(EnregistrementChien,EnregistrementChienAdmin)