# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchBac'
        db.create_table(u'searchbac_searchbac', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'searchbac', ['SearchBac'])


    def backwards(self, orm):
        # Deleting model 'SearchBac'
        db.delete_table(u'searchbac_searchbac')


    models = {
        u'searchbac.searchbac': {
            'Meta': {'object_name': 'SearchBac'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['searchbac']