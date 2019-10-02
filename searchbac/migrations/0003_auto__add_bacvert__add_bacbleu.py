# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BacVert'
        db.create_table(u'searchbac_bacvert', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['BacVert'])

        # Adding model 'BacBleu'
        db.create_table(u'searchbac_bacbleu', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['BacBleu'])


    def backwards(self, orm):
        # Deleting model 'BacVert'
        db.delete_table(u'searchbac_bacvert')

        # Deleting model 'BacBleu'
        db.delete_table(u'searchbac_bacbleu')


    models = {
        u'searchbac.bacbleu': {
            'Meta': {'object_name': 'BacBleu', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.bacbrun': {
            'Meta': {'object_name': 'BacBrun', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.bacvert': {
            'Meta': {'object_name': 'BacVert', '_ormbases': [u'searchbac.BaseBac']},
            u'basebac_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['searchbac.BaseBac']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'searchbac.basebac': {
            'Meta': {'object_name': 'BaseBac'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        },
        u'searchbac.searchbac': {
            'Meta': {'object_name': 'SearchBac'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['searchbac']