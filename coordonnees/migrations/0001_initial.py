# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coordonnees'
        db.create_table(u'coordonnees_coordonnees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('contact_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('address', self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'coordonnees', ['Coordonnees'])


    def backwards(self, orm):
        # Deleting model 'Coordonnees'
        db.delete_table(u'coordonnees_coordonnees')


    models = {
        u'coordonnees.coordonnees': {
            'Meta': {'object_name': 'Coordonnees'},
            'address': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['coordonnees']