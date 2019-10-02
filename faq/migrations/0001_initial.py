# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'faq_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
        ))
        db.send_create_signal(u'faq', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'faq_news')


    models = {
        u'faq.news': {
            'Meta': {'object_name': 'News'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['faq']