# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BaseDocument._order'
        db.delete_column(u'documentation_basedocument', '_order')


    def backwards(self, orm):
        # Adding field 'BaseDocument._order'
        db.add_column(u'documentation_basedocument', '_order',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    models = {
        u'documentation.basecategory': {
            'Meta': {'object_name': 'BaseCategory'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            's_text': ('mezzanine.core.fields.RichTextField', [], {}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'documentation.basedocument': {
            'Meta': {'object_name': 'BaseDocument'},
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        },
        u'documentation.polenviroregmun': {
            'Meta': {'object_name': 'PolEnviroRegMun', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'categorie': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'documentation.procesverbauxconseil': {
            'Meta': {'object_name': 'ProcesVerbauxConseil', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['documentation']