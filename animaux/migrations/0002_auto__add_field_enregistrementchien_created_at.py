# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EnregistrementChien.created_at'
        db.add_column(u'animaux_enregistrementchien', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2017, 4, 27, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EnregistrementChien.created_at'
        db.delete_column(u'animaux_enregistrementchien', 'created_at')


    models = {
        u'animaux.enregistrementchien': {
            'Meta': {'object_name': 'EnregistrementChien'},
            'chien2_active': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_age': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_couleur1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_couleur2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_marques': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'chien2_micropuce': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_race1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_race1_autre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_race2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_race2_autre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_sexe': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_sterilisation_clinique_adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_sterilisation_clinique_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_sterilisation_clinique_telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien2_sterilise': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_age': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chien_couleur1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chien_couleur2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_marques': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'chien_micropuce': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chien_race1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chien_race1_autre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_race2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_race2_autre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_sexe': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chien_sterilisation_clinique_adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_sterilisation_clinique_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_sterilisation_clinique_telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chien_sterilise': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proprietaire_adresse_app': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'proprietaire_adresse_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_adresse_no_civique': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_adresse_rue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_courriel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietaire_telephone_secondaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['animaux']