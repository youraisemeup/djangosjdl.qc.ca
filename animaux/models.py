#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class EnregistrementChien(models.Model):
    tuple_none = [('', 'Aucune')]

    choix_races = [
        (u'Affenpinscher', u'Affenpinscher'), (u'Akita', u'Akita'),
        (u'American Staffordshire', u'American Staffordshire'), (u'Basenji', u'Basenji'), (u'Basset', u'Basset'),
        (u'Beagle', u'Beagle'), (u'Bearded Collie', u'Bearded Collie'), (u'Beauceron', u'Beauceron'),
        (u'Bedlington Terrier', u'Bedlington Terrier'), (u'Berger', u'Berger'),
        (u'Berger Allemand', u'Berger Allemand'), (u'Berger Anglais', u'Berger Anglais'),
        (u'Berger Australien', u'Berger Australien'), (u'Berger Belge', u'Berger Belge'),
        (u'Berger Shetland', u'Berger Shetland'), (u'Bichon frisé', u'Bichon frisé'),
        (u'Bichon Maltais', u'Bichon Maltais'), (u'Bloodhound', u'Bloodhound'), (u'Blue Heeler', u'Blue Heeler'),
        (u'Border Collie', u'Border Collie'), (u'Borzoï', u'Borzoï'), (u'Boston Terrier', u'Boston Terrier'),
        (u'Bouledogue Américain', u'Bouledogue Américain'), (u'Bouledogue Anglais', u'Bouledogue Anglais'),
        (u'Bouledogue Français', u'Bouledogue Français'), (u'Bouvier Bernois', u'Bouvier Bernois'),
        (u'Bouvier des Flandres', u'Bouvier des Flandres'), (u'Boxer', u'Boxer'),
        (u'Braque Allemand', u'Braque Allemand'), (u'Braque de Weimar', u'Braque de Weimar'), (u'Briard', u'Briard'),
        (u'Bull Terrier', u'Bull Terrier'), (u'Bullmastiffs', u'Bullmastiffs'), (u'Cairn Terrier', u'Cairn Terrier'),
        (u'Cana Corso', u'Cana Corso'), (u'Caniche', u'Caniche'), (u'Caniche Miniature', u'Caniche Miniature'),
        (u'Caniche Moyen', u'Caniche Moyen'), (u'Caniche Miniature', u'Caniche Miniature'),
        (u'Caniche Royal', u'Caniche Royal'), (u'Carlin (Pug)', u'Carlin (Pug)'),
        (u'Cavalier King Charles', u'Cavalier King Charles'), (u'Chien chinois à crête', u'Chien chinois à crête'),
        (u'Chihuahua', u'Chihuahua'), (u'Chow Chow', u'Chow Chow'), (u'Cockapoo', u'Cockapoo'), (u'Collie', u'Collie'),
        (u'Coonhound', u'Coonhound'), (u'Corgi', u'Corgi'), (u'Coton de Tuléar', u'Coton de Tuléar'),
        (u'Dachshund (Teckel)', u'Dachshund (Teckel)'), (u'Dalmatien', u'Dalmatien'), (u'Doberman', u'Doberman'),
        (u'Dogo Argentino', u'Dogo Argentino'),
        (u'Dogue de Bordeaux', u'Dogue de Bordeaux'), (u'Dogue du Tibet', u'Dogue du Tibet'),
        (u'Épagneul', u'Épagneul'), (u'Épagneul (Cocker Américain)', u'Épagneul (Cocker Américain)'),
        (u'Épagneul (Spriger Anglais)', u'Épagneul (Spriger Anglais)'),
        (u'Esquimau Américain', u'Esquimau Américain'),
        (u'Flat0Coated Retriver', u'Flat0Coated Retriver'), (u'Fox Terrier', u'Fox Terrier'),
        (u'Golden Retriever', u'Golden Retriever'), (u'Gordon Setter', u'Gordon Setter'),
        (u'Grand Danois', u'Grand Danois'), (u'Griffon Bruxellois', u'Griffon Bruxellois'),
        (u'Griffon d’arrêt à poil dur', u'Griffon d’arrêt à poil dur'), (u'Havanais', u'Havanais'),
        (u'Huski Sibérien', u'Huski Sibérien'),
        (u'Jack Russell Terrier', u'Jack Russell Terrier'), (u'Keeshond', u'Keeshond'),
        (u'Kerry Blue Terrier', u'Kerry Blue Terrier'), (u'Komondor', u'Komondor'),
        (u'Labrador retriever', u'Labrador retriever'), (u'Leonberger', u'Leonberger'),
        (u'Lévrier Afghan', u'Lévrier Afghan'), (u'Lévier Anglais', u'Lévier Anglais'),
        (u'Lhasa Apso', u'Lhasa Apso'), (u'Malamute', u'Malamute'), (u'Mâtin Napolitain', u'Mâtin Napolitain'),
        (u'Montagne des Pyrénées', u'Montagne des Pyrénées'), (u'Papillon', u'Papillon'),
        (u'Parson Russell Terrier', u'Parson Russell Terrier'), (u'Pékinois', u'Pékinois'),
        (u'Petit Bassett Griffon Vendéen', u'Petit Bassett Griffon Vendéen'),
        (u'Pinscher Miniature', u'Pinscher Miniature'), (u'Pit Bull Terrier', u'Pit Bull Terrier'),
        (u'Pointer', u'Pointer'), (u'Poméranien', u'Poméranien'), (u'Presa Canario', u'Presa Canario'),
        (u'Puli', u'Puli'), (u' Rhodesian Ridgeback', u' Rhodesian Ridgeback'), (u'Rottweiler', u'Rottweiler'),
        (u'Saint-Bernard', u'Saint-Bernard'), (u'Saluki', u'Saluki'), (u'Samoyède', u'Samoyède'),
        (u'Schnauzer Géant', u'Schnauzer Géant'), (u'Schnauzer Nain', u'Schnauzer Nain'),
        (u'Schnauzer Standard', u'Schnauzer Standard'), (u'Setter Irlandais', u'Setter Irlandais'),
        (u'Shar Pei', u'Shar Pei'), (u'Shiba Inu', u'Shiba Inu'), (u'Shih Tzu', u'Shih Tzu'), (u'Spitz', u'Spitz'),
        (u'Staffordshire Bull Terrier', u'Staffordshire Bull Terrier'),
        (u'Terre-Neuve', u'Terre-Neuve'), (u'Terrier', u'Terrier'),
        (u'Terrier de Manchester', u'Terrier de Manchester'), (u'Terrier Écossais', u'Terrier Écossais'),
        (u'Terrier Irlandais', u'Terrier Irlandais'), (u'Vizsla', u'Vizsla'),
        (u'Welsh Corgi', u'Welsh Corgi'), (u'West Highland Terrier (Westie)', u'West Highland Terrier (Westie)'),
        (u'Wheaten Terrier', u'Wheaten Terrier'), (u'Whippet', u'Whippet'),
        (u'Yorkshire Terrier (Yorkie)', u'Yorkshire Terrier (Yorkie)'), ('Autre', 'Autre')
    ]

    choix_races_none = tuple_none + choix_races

    choix_couleurs = [
        (u'Abrico', u'Abrico'), (u'Arlequin', u'Arlequin'), (u'Beige', u'Beige'), (u'Blanc', u'Blanc'),
        (u'Bleu', u'Bleu'), (u'Blond', u'Blond'), (u'Bringé', u'Bringé'), (u'Brun', u'Brun'),
        (u'Chocolat', u'Chocolat'), (u'Crème', u'Crème'), (u'Doré', u'Doré'), (u'Fauve', u'Fauve'), (u'Feu', u'Feu'),
        (u'Gris', u'Gris'), (u'Merle', u'Merle'), (u'Noir', u'Noir'), (u'Roux', u'Roux'), (u'Sable', u'Sable'),
        (u'Tricolore (Noir, blanc et roux)', u'Tricolore (Noir, blanc et roux)')
    ]

    choix_couleurs_none = tuple_none + choix_couleurs

    choix_age = (
        (u'1 mois', u'1 mois'), (u'2 mois', u'2 mois'), (u'3 mois', u'3 mois'), (u'4 mois', u'4 mois'),
        (u'5 mois', u'5 mois'), (u'6 mois', u'6 mois'), (u'7 mois', u'7 mois'), (u'8 mois', u'8 mois'),
        (u'9 mois', u'9 mois'), (u'10 mois', u'10 mois'), (u'11 mois', u'11 mois'), (u'1 an', u'1 an'),
        (u'2 ans', u'2 ans'), (u'3 ans', u'3 ans'), (u'4 ans', u'4 ans'), (u'5 ans', u'5 ans'), (u'6 ans', u'6 ans'),
        (u'7 ans', u'7 ans'), (u'8 ans', u'8 ans'), (u'9 ans', u'9 ans'), (u'10 ans', u'10 ans'),
        (u'11 ans', u'11 ans'), (u'12 ans', u'12 ans'), (u'13 ans', u'13 ans'), (u'14 ans', u'14 ans'),
        (u'15 ans', u'15 ans'), (u'16 ans', u'16 ans')
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # Propriétaire 1
    proprietaire_prenom = models.CharField('Prénom', max_length=255)
    proprietaire_nom = models.CharField('Nom', max_length=255)
    proprietaire_telephone = models.CharField('Téléphone', max_length=255)
    proprietaire_telephone_secondaire = models.CharField('Téléphone secondaire', max_length=255, blank=True)
    proprietaire_courriel = models.CharField('Courriel', max_length=255)

    proprietaire_adresse_no_civique = models.CharField('No civique', max_length=255)
    proprietaire_adresse_rue = models.CharField('Rue', max_length=255)
    proprietaire_adresse_app = models.CharField('App. / C.P.', max_length=255, blank=True)
    proprietaire_adresse_code_postal = models.CharField('Code postal', max_length=255)

    # Propriétaire 2
    """proprietaire2_active = forms.ChoiceField(
        label='',
        choices=(
            ('1', '1'),
            ('', '0')
        ),
        blank=True,
        widget=forms.HiddenInput()
    )
    proprietaire2_prenom = forms.CharField(label='Prénom')
    proprietaire2_nom = forms.CharField(label='Nom')
    proprietaire2_telephone = forms.CharField(label='Téléphone')
    proprietaire2_telephone_secondaire = forms.CharField(label='Téléphone secondaire', blank=True)
    proprietaire2_courriel = forms.CharField(label='Courriel', blank=True)

    proprietaire2_adresse_no_civique = forms.CharField(label='No civique')
    proprietaire2_adresse_rue = forms.CharField(label='Rue')
    proprietaire2_adresse_app = forms.CharField(label='App. / C.P.', blank=True)
    proprietaire2_adresse_code_postal = forms.CharField(label='Code postal')
    """
    # Chien 1
    chien_sexe = models.CharField(
        'Sexe',
        max_length=255,
        choices=(
            (u'Mâle', 'Mâle'),
            (u'Femelle', 'Femelle'),
        )
    )
    chien_sterilise = models.CharField(
        'Stérilisé?',
        max_length=255,
        choices=(
            (u'oui', 'Oui'),
            (u'non', 'Non'),
        )
    )
    chien_nom = models.CharField('Nom', max_length=255)
    chien_micropuce = models.CharField('Numéro de micropuce (si micropucé)', max_length=255, blank=True)
    chien_age = models.CharField(
        "Âge",
        max_length=255,
        choices=choix_age
    )
    chien_couleur1 = models.CharField(
        "Couleur principale",
        max_length=255,
        choices=choix_couleurs
    )
    chien_couleur2 = models.CharField(
        "Couleur secondaire",
        max_length=255,
        choices=choix_couleurs_none,
        blank=True
    )
    chien_race1 = models.CharField(
        "Race principale",
        max_length=255,
        choices=choix_races
    )
    chien_race1_autre = models.CharField(
        "Race principale (autre)",
        max_length=255,
        blank=True
    )
    chien_race2 = models.CharField(
        "Race secondaire",
        choices=choix_races_none,
        max_length=255,
        blank=True
    )
    chien_race2_autre = models.CharField(
        "Race secondaire (autre)",
        max_length=255,
        blank=True
    )
    chien_marques = models.TextField('Est-ce que votre chien porte des marques distinctives?', blank=True)

    chien_sterilisation_clinique_nom = models.CharField('Nom de la clinique vétérinaire', max_length=255, blank=True)
    chien_sterilisation_clinique_adresse = models.CharField('Adresse de la clinique vétérinaire', max_length=255, blank=True)
    chien_sterilisation_clinique_telephone = models.CharField('Téléphone de la clinique vétérinaire', max_length=255, blank=True)

    # Chien 1
    chien2_active = models.CharField(
        '',
        max_length=255,
        choices=(
            ('1', '1'),
            ('', '0')
        ),
        blank=True
    )
    chien2_sexe = models.CharField(
        'Sexe',
        max_length=255,
        choices=(
            (u'Mâle', 'Mâle'),
            (u'Femelle', 'Femelle'),
        ),
        blank=True
    )
    chien2_sterilise = models.CharField(
        'Stérilisé?',
        max_length=255,
        choices=(
            (u'oui', 'Oui'),
            (u'non', 'Non'),
        ),
        blank=True
    )
    chien2_nom = models.CharField('Nom', max_length=255, blank=True)
    chien2_micropuce = models.CharField('Numéro de micropuce (si micropucé)', max_length=255, blank=True)
    chien2_age = models.CharField(
        "Âge",
        max_length=255,
        choices=choix_age,
        blank=True
    )
    chien2_couleur1 = models.CharField(
        "Couleur principale",
        max_length=255,
        choices=choix_couleurs,
        blank=True
    )
    chien2_couleur2 = models.CharField(
        "Couleur secondaire",
        max_length=255,
        choices=choix_couleurs_none,
        blank=True
    )
    chien2_race1 = models.CharField(
        "Race principale",
        max_length=255,
        choices=choix_races,
        blank=True
    )
    chien2_race1_autre = models.CharField(
        "Race principale (autre)",
        max_length=255,
        blank=True
    )
    chien2_race2 = models.CharField(
        "Race secondaire",
        max_length=255,
        choices=choix_races_none,
        blank=True
    )
    chien2_race2_autre = models.CharField(
        "Race secondaire (autre)",
        max_length=255,
        blank=True
    )
    chien2_marques = models.TextField('Est-ce que votre chien porte des marques distinctives?', blank=True)

    chien2_sterilisation_clinique_nom = models.CharField('Nom de la clinique vétérinaire', max_length=255, blank=True)
    chien2_sterilisation_clinique_adresse = models.CharField('Adresse de la clinique vétérinaire', max_length=255, blank=True)
    chien2_sterilisation_clinique_telephone = models.CharField('Téléphone de la clinique vétérinaire', max_length=255, blank=True)

    def __unicode__(self):
        return self.proprietaire_prenom + ' ' + self.proprietaire_nom

    def get_proprietaire(self):
        return self.proprietaire_prenom + ' ' + self.proprietaire_nom

    get_proprietaire.short_description = "Nom du propriétaire"

    class Meta:
        verbose_name = 'Enregistrement chien'
        verbose_name_plural = 'Enregistrements chiens'


EnregistrementChien._meta.get_field('created_at').verbose_name = "Date de création"