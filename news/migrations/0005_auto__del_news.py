# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')


    def backwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            ('s_text', self.gf('django.db.models.fields.TextField')()),
            ('dt_end', self.gf('django.db.models.fields.DateField')()),
            ('s_link_youtube', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('s_link_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt_begin', self.gf('django.db.models.fields.DateField')()),
            ('s_excerpt_home', self.gf('django.db.models.fields.TextField')(max_length=150, null=True, blank=True)),
            ('s_link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('s_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ik_image', self.gf('mezzanine.core.fields.FileField')(max_length=200, null=True, blank=True)),
            ('ik_diapo', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['galleries.Gallery'], null=True, blank=True)),
            ('ik_home_image', self.gf('mezzanine.core.fields.FileField')(max_length=200, null=True, blank=True)),
            ('b_home', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'news', ['News'])


    models = {
        
    }

    complete_apps = ['news']