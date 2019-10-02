# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('s_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('s_text', self.gf('django.db.models.fields.TextField')()),
            ('ik_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('s_link', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('s_link_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            ('dt_begin', self.gf('django.db.models.fields.DateField')()),
            ('dt_end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'news', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')


    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'dt_begin': ('django.db.models.fields.DateField', [], {}),
            'dt_end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ik_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            's_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            's_link_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            's_text': ('django.db.models.fields.TextField', [], {}),
            's_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']