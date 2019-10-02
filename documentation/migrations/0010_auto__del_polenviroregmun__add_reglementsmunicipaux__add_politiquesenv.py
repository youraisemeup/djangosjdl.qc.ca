# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PolEnviroRegMun'
        db.delete_table(u'documentation_polenviroregmun')

        # Adding model 'ReglementsMunicipaux'
        db.create_table(u'documentation_reglementsmunicipaux', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
            ('text', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'documentation', ['ReglementsMunicipaux'])

        # Adding model 'PolitiquesEnvironnementales'
        db.create_table(u'documentation_politiquesenvironnementales', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['PolitiquesEnvironnementales'])


    def backwards(self, orm):
        # Adding model 'PolEnviroRegMun'
        db.create_table(u'documentation_polenviroregmun', (
            ('categorie', self.gf('django.db.models.fields.IntegerField')(default=1)),
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['PolEnviroRegMun'])

        # Deleting model 'ReglementsMunicipaux'
        db.delete_table(u'documentation_reglementsmunicipaux')

        # Deleting model 'PolitiquesEnvironnementales'
        db.delete_table(u'documentation_politiquesenvironnementales')


    models = {
        u'documentation.avispublics': {
            'Meta': {'object_name': 'AvisPublics', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
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
        u'documentation.bulletinsmunicipaux': {
            'Meta': {'object_name': 'BulletinsMunicipaux', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'documentation.calendriersmunicipaux': {
            'Meta': {'object_name': 'CalendriersMunicipaux', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.communiquespresse': {
            'Meta': {'object_name': 'CommuniquesPresse', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.informationsfinancieres': {
            'Meta': {'object_name': 'InformationsFinancieres', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'categorie': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'documentation.politiquesenvironnementales': {
            'Meta': {'object_name': 'PolitiquesEnvironnementales', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.procesverbauxconseil': {
            'Meta': {'object_name': 'ProcesVerbauxConseil', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.procesverbauxregieassainissement': {
            'Meta': {'object_name': 'ProcesVerbauxRegieAssainissement', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.procesverbauxregietraitement': {
            'Meta': {'object_name': 'ProcesVerbauxRegieTraitement', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.reglementsmunicipaux': {
            'Meta': {'object_name': 'ReglementsMunicipaux', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('mezzanine.core.fields.RichTextField', [], {})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['documentation']