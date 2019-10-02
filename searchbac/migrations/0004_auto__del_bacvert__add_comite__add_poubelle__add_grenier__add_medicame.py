# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BacVert'
        db.delete_table(u'searchbac_bacvert')

        # Adding model 'Comite'
        db.create_table(u'searchbac_comite', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Comite'])

        # Adding model 'Poubelle'
        db.create_table(u'searchbac_poubelle', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Poubelle'])

        # Adding model 'Grenier'
        db.create_table(u'searchbac_grenier', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Grenier'])

        # Adding model 'Medicaments'
        db.create_table(u'searchbac_medicaments', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Medicaments'])

        # Adding model 'Joujou'
        db.create_table(u'searchbac_joujou', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Joujou'])

        # Adding model 'Arbres'
        db.create_table(u'searchbac_arbres', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['Arbres'])


    def backwards(self, orm):
        # Adding model 'BacVert'
        db.create_table(u'searchbac_bacvert', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['BacVert'])

        # Deleting model 'Comite'
        db.delete_table(u'searchbac_comite')

        # Deleting model 'Poubelle'
        db.delete_table(u'searchbac_poubelle')

        # Deleting model 'Grenier'
        db.delete_table(u'searchbac_grenier')

        # Deleting model 'Medicaments'
        db.delete_table(u'searchbac_medicaments')

        # Deleting model 'Joujou'
        db.delete_table(u'searchbac_joujou')

        # Deleting model 'Arbres'
        db.delete_table(u'searchbac_arbres')


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