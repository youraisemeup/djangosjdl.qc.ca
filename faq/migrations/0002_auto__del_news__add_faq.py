# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'faq_news')

        # Adding model 'Faq'
        db.create_table(u'faq_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
        ))
        db.send_create_signal(u'faq', ['Faq'])


    def backwards(self, orm):
        # Adding model 'News'
        db.create_table(u'faq_news', (
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
        ))
        db.send_create_signal(u'faq', ['News'])

        # Deleting model 'Faq'
        db.delete_table(u'faq_faq')


    models = {
        u'faq.faq': {
            'Meta': {'object_name': 'Faq'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        }
    }

    complete_apps = ['faq']