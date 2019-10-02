# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AvisPublics'
        db.create_table(u'documentation_avispublics', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['AvisPublics'])

        # Adding model 'BulletinsMunicipaux'
        db.create_table(u'documentation_bulletinsmunicipaux', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'documentation', ['BulletinsMunicipaux'])

        # Adding model 'ProcesVerbauxRegieTraitement'
        db.create_table(u'documentation_procesverbauxregietraitement', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['ProcesVerbauxRegieTraitement'])

        # Adding model 'InformationsFinancieres'
        db.create_table(u'documentation_informationsfinancieres', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
            ('categorie', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'documentation', ['InformationsFinancieres'])

        # Adding model 'CalendriersMunicipaux'
        db.create_table(u'documentation_calendriersmunicipaux', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['CalendriersMunicipaux'])

        # Adding model 'ProcesVerbauxRegieAssainissement'
        db.create_table(u'documentation_procesverbauxregieassainissement', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['ProcesVerbauxRegieAssainissement'])


    def backwards(self, orm):
        # Deleting model 'AvisPublics'
        db.delete_table(u'documentation_avispublics')

        # Deleting model 'BulletinsMunicipaux'
        db.delete_table(u'documentation_bulletinsmunicipaux')

        # Deleting model 'ProcesVerbauxRegieTraitement'
        db.delete_table(u'documentation_procesverbauxregietraitement')

        # Deleting model 'InformationsFinancieres'
        db.delete_table(u'documentation_informationsfinancieres')

        # Deleting model 'CalendriersMunicipaux'
        db.delete_table(u'documentation_calendriersmunicipaux')

        # Deleting model 'ProcesVerbauxRegieAssainissement'
        db.delete_table(u'documentation_procesverbauxregieassainissement')


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
        u'documentation.informationsfinancieres': {
            'Meta': {'object_name': 'InformationsFinancieres', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'categorie': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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
        u'documentation.procesverbauxregieassainissement': {
            'Meta': {'object_name': 'ProcesVerbauxRegieAssainissement', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.procesverbauxregietraitement': {
            'Meta': {'object_name': 'ProcesVerbauxRegieTraitement', '_ormbases': [u'documentation.BaseDocument']},
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