# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RepertoryLinks.usefullink_category'
        db.alter_column(u'usefullinks_repertorylinks', 'usefullink_category', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'RepertoryLinks.usefullink_category'
        db.alter_column(u'usefullinks_repertorylinks', 'usefullink_category', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'usefullinks.baselinks': {
            'Meta': {'object_name': 'BaseLinks'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contactname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'excerpt': ('mezzanine.core.fields.RichTextField', [], {}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.CharField', [], {'default': "u'Organisation'", 'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'usefullinks.repertorylinks': {
            'Meta': {'object_name': 'RepertoryLinks', '_ormbases': [u'usefullinks.BaseLinks']},
            u'baselinks_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['usefullinks.BaseLinks']", 'unique': 'True', 'primary_key': 'True'}),
            'repertory_category': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'usefullink_category': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'usefullinks.usefullinks': {
            'Meta': {'object_name': 'UsefulLinks', '_ormbases': [u'usefullinks.BaseLinks']},
            u'baselinks_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['usefullinks.BaseLinks']", 'unique': 'True', 'primary_key': 'True'}),
            'categorie': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['usefullinks']