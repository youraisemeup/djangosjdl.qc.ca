# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseBac'
        db.create_table(u'searchbac_basebac', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'searchbac', ['BaseBac'])

        # Adding model 'BacBrun'
        db.create_table(u'searchbac_bacbrun', (
            (u'basebac_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['searchbac.BaseBac'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'searchbac', ['BacBrun'])


    def backwards(self, orm):
        # Deleting model 'BaseBac'
        db.delete_table(u'searchbac_basebac')

        # Deleting model 'BacBrun'
        db.delete_table(u'searchbac_bacbrun')


    models = {
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
        u'searchbac.searchbac': {
            'Meta': {'object_name': 'SearchBac'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['searchbac']