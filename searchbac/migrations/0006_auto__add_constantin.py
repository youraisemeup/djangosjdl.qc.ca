# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Constantin'
        db.create_table(u'searchbac_constantin', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Constantin'])


    def backwards(self, orm):
        # Deleting model 'Constantin'
        db.delete_table(u'searchbac_constantin')


    models = {
        u'searchbac.arbres': {
            'Meta': {'object_name': 'Arbres', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.bacbleu': {
            'Meta': {'object_name': 'BacBleu', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.bacbrun': {
            'Meta': {'object_name': 'BacBrun', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.basebac': {
            'Meta': {'object_name': 'BaseBac'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        },
        u'searchbac.comite': {
            'Meta': {'object_name': 'Comite', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.constantin': {
            'Meta': {'object_name': 'Constantin', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.ecocentre': {
            'Meta': {'object_name': 'Ecocentre', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.grenier': {
            'Meta': {'object_name': 'Grenier', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.joujou': {
            'Meta': {'object_name': 'Joujou', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.medicaments': {
            'Meta': {'object_name': 'Medicaments', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.poubelle': {
            'Meta': {'object_name': 'Poubelle', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.searchbac': {
            'Meta': {'object_name': 'SearchBac'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['searchbac']