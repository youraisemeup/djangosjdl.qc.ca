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
            ('s_link', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dt_begin', self.gf('django.db.models.fields.DateField')()),
            ('s_text', self.gf('django.db.models.fields.TextField')()),
            ('s_link_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dt_end', self.gf('django.db.models.fields.DateField')()),
            ('s_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ik_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'news', ['News'])


    models = {
        
    }

    complete_apps = ['news']