#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django import forms
from sjdl.animaux.models import EnregistrementChien

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, Div, HTML, Button
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions, InlineCheckboxes, InlineRadios)

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

class EnregistrementChienForm(forms.ModelForm):

    helper = FormHelper()

    helper.form_method = "POST"
    helper.layout = Layout(
        Fieldset(
            u"Propriétaire de l'animal",

            Div(
                Div(
                    Div("proprietaire_prenom", css_class="col-sm-12"),
                    Div("proprietaire_nom", css_class="col-sm-12"),
                    Div("proprietaire_telephone", css_class="col-sm-12"),
                    Div("proprietaire_telephone_secondaire", css_class="col-sm-12"),
                    Div("proprietaire_courriel", css_class="col-sm-12"),
                    css_class="col-sm-6"
                ),
                Div(
                    Div("proprietaire_adresse_no_civique", css_class="col-sm-12"),
                    Div("proprietaire_adresse_rue", css_class="col-sm-12"),
                    Div("proprietaire_adresse_app", css_class="col-sm-12"),
                    Div("proprietaire_adresse_code_postal", css_class="col-sm-12"),
                    css_class="col-sm-6"
                ),
                css_class="row"
            ),
            css_class="proprietaire"
        ),

        Fieldset(
            u"Identification du chien",

            Div(
                Div(
                    Div("chien_nom", css_class="col-sm-12"),
                    Div("chien_sexe", css_class="col-sm-12"),
                    Div("chien_sterilise", css_class="col-sm-12"),
                    Div("chien_age", css_class="col-sm-12"),
                    Div("chien_race1", css_class="chien_race1 col-sm-12"),
                    Div("chien_race1_autre", css_class="autre chien_race1_autre col-sm-12"),
                    Div("chien_race2", css_class="chien_race2 col-sm-12"),
                    Div("chien_race2_autre", css_class="autre chien_race2_autre col-sm-12"),
                    css_class="col-sm-6"
                ),
                Div(
                    Div("chien_couleur1", css_class="col-sm-12"),
                    Div("chien_couleur2", css_class="col-sm-12"),
                    Div("chien_micropuce", css_class="col-sm-12"),
                    Div("chien_marques", css_class="col-sm-12"),
                    css_class="col-sm-6"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    HTML(u"""<h4>Stérilisation</h4>"""),
                    Div("chien_sterilisation_clinique_nom", css_class="col-sm-12"),
                    Div("chien_sterilisation_clinique_adresse", css_class="col-sm-12"),
                    Div("chien_sterilisation_clinique_telephone", css_class="col-sm-12"),
                ),
                css_class="row sterilisation"
            ),
            css_class="chien1"
        ),
        HTML(u"""<button type="button" id="add_dog">Ajouter un second chien</button>"""),
        Fieldset(
            u"Identification du second chien",

            HTML(u"""<button type="button" id="remove_dog">Retirer ce chien</button>"""),
            Field('chien2_active', type="hidden"),
            Div(
                Div(
                    Div("chien2_nom", css_class="col-sm-12"),
                    Div("chien2_sexe", css_class="col-sm-12"),
                    Div("chien2_sterilise", css_class="col-sm-12"),
                    Div("chien2_age", css_class="col-sm-12"),
                    Div("chien2_race1", css_class="chien2_race1 col-sm-12"),
                    Div("chien2_race1_autre", css_class="autre chien2_race1_autre col-sm-12"),
                    Div("chien2_race2", css_class="chien2_race2 col-sm-12"),
                    Div("chien2_race2_autre", css_class="autre chien2_race2_autre col-sm-12"),
                    css_class="col-sm-6"
                ),
                Div(
                    Div("chien2_couleur1", css_class="col-sm-12"),
                    Div("chien2_couleur2", css_class="col-sm-12"),
                    Div("chien2_micropuce", css_class="col-sm-12"),
                    Div("chien2_marques", css_class="col-sm-12"),
                    css_class="col-sm-6"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    HTML(u"""<h4>Stérilisation</h4>"""),
                    Div("chien2_sterilisation_clinique_nom", css_class="col-sm-12"),
                    Div("chien2_sterilisation_clinique_adresse", css_class="col-sm-12"),
                    Div("chien2_sterilisation_clinique_telephone", css_class="col-sm-12"),
                ),
                css_class="row sterilisation"
            ),
            css_class="chien2"
        ),
    )

    helper.add_input(
        Submit("btnSoumettre", "Soumettre", css_class="more")
    )

    class Meta:
        model = EnregistrementChien

    def __init__(self, data=None, *args, **kwargs):
        super(EnregistrementChienForm, self).__init__(data, *args, **kwargs)

        if data:

            # Si pas de second propriétaire
            """
            if data.get('proprietaire2_active') != '1':
                self.fields['proprietaire2_prenom'].required = False
                self.fields['proprietaire2_nom'].required = False
                self.fields['proprietaire2_telephone'].required = False
                self.fields['proprietaire2_telephone_secondaire'].required = False
                self.fields['proprietaire2_courriel'].required = False
                self.fields['proprietaire2_adresse_no_civique'].required = False
                self.fields['proprietaire2_adresse_rue'].required = False
                self.fields['proprietaire2_adresse_app'].required = False
                self.fields['proprietaire2_adresse_code_postal'].required = False
            """

            if data.get('chien_race1') == 'Autre':
                self.fields['chien_race1_autre'].required = True

            if data.get('chien_race2') == 'Autre':
                self.fields['chien_race2_autre'].required = True

            if data.get('chien2_race1') == 'Autre':
                self.fields['chien2_race1_autre'].required = True

            if data.get('chien2_race2') == 'Autre':
                self.fields['chien2_race2_autre'].required = True

            if data.get('chien_sterilise') == 'oui':
                self.fields['chien_sterilisation_clinique_nom'].required = True
                self.fields['chien_sterilisation_clinique_adresse'].required = True
                self.fields['chien_sterilisation_clinique_telephone'].required = True

            if data.get('chien2_active') == '1':
                if data.get('chien2_sterilise') == 'oui':
                    self.fields['chien2_sterilisation_clinique_nom'].required = True
                    self.fields['chien2_sterilisation_clinique_adresse'].required = True
                    self.fields['chien2_sterilisation_clinique_telephone'].required = True

                self.fields['chien2_nom'].required = True
                self.fields['chien2_sexe'].required = True
                self.fields['chien2_sterilise'].required = True
                self.fields['chien2_age'].required = True
                self.fields['chien2_race1'].required = True
                self.fields['chien2_couleur1'].required = True

    def send_email(self):

        email_content = render_to_string('email/enregistrement_chien.html', {'form': self})

        msg = EmailMessage(settings.ENREGISTREMENT_CHIEN_EMAIL_SUBJECT,
                           email_content,
                           settings.ENREGISTREMENT_CHIEN_EMAIL_ADDRESS_FROM,
                           [settings.ENREGISTREMENT_CHIEN_EMAIL_ADDRESS_TO])
        msg.content_subtype = "html"

        msg.send(fail_silently=False)