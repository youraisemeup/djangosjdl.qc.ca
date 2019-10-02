# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BaseCategory'
        db.delete_table(u'documentation_basecategory')

        # Deleting field 'ReglementsMunicipaux.text'
        db.delete_column(u'documentation_reglementsmunicipaux', 'text')

        # Adding field 'ReglementsMunicipaux.keywords_string'
        db.add_column(u'documentation_reglementsmunicipaux', u'keywords_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.site'
        db.add_column(u'documentation_reglementsmunicipaux', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.slug'
        db.add_column(u'documentation_reglementsmunicipaux', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux._meta_title'
        db.add_column(u'documentation_reglementsmunicipaux', '_meta_title',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.description'
        db.add_column(u'documentation_reglementsmunicipaux', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.gen_description'
        db.add_column(u'documentation_reglementsmunicipaux', 'gen_description',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.created'
        db.add_column(u'documentation_reglementsmunicipaux', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.updated'
        db.add_column(u'documentation_reglementsmunicipaux', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.status'
        db.add_column(u'documentation_reglementsmunicipaux', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.expiry_date'
        db.add_column(u'documentation_reglementsmunicipaux', 'expiry_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.short_url'
        db.add_column(u'documentation_reglementsmunicipaux', 'short_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReglementsMunicipaux.in_sitemap'
        db.add_column(u'documentation_reglementsmunicipaux', 'in_sitemap',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'ReglementsMunicipaux.publish_date'
        db.alter_column(u'documentation_reglementsmunicipaux', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'ReglementsMunicipaux.title'
        db.alter_column(u'documentation_reglementsmunicipaux', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):
        # Adding model 'BaseCategory'
        db.create_table(u'documentation_basecategory', (
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('s_text', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'documentation', ['BaseCategory'])


        # User chose to not deal with backwards NULL issues for 'ReglementsMunicipaux.text'
        raise RuntimeError("Cannot reverse this migration. 'ReglementsMunicipaux.text' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ReglementsMunicipaux.text'
        db.add_column(u'documentation_reglementsmunicipaux', 'text',
                      self.gf('mezzanine.core.fields.RichTextField')(),
                      keep_default=False)

        # Deleting field 'ReglementsMunicipaux.keywords_string'
        db.delete_column(u'documentation_reglementsmunicipaux', u'keywords_string')

        # Deleting field 'ReglementsMunicipaux.site'
        db.delete_column(u'documentation_reglementsmunicipaux', 'site_id')

        # Deleting field 'ReglementsMunicipaux.slug'
        db.delete_column(u'documentation_reglementsmunicipaux', 'slug')

        # Deleting field 'ReglementsMunicipaux._meta_title'
        db.delete_column(u'documentation_reglementsmunicipaux', '_meta_title')

        # Deleting field 'ReglementsMunicipaux.description'
        db.delete_column(u'documentation_reglementsmunicipaux', 'description')

        # Deleting field 'ReglementsMunicipaux.gen_description'
        db.delete_column(u'documentation_reglementsmunicipaux', 'gen_description')

        # Deleting field 'ReglementsMunicipaux.created'
        db.delete_column(u'documentation_reglementsmunicipaux', 'created')

        # Deleting field 'ReglementsMunicipaux.updated'
        db.delete_column(u'documentation_reglementsmunicipaux', 'updated')

        # Deleting field 'ReglementsMunicipaux.status'
        db.delete_column(u'documentation_reglementsmunicipaux', 'status')

        # Deleting field 'ReglementsMunicipaux.expiry_date'
        db.delete_column(u'documentation_reglementsmunicipaux', 'expiry_date')

        # Deleting field 'ReglementsMunicipaux.short_url'
        db.delete_column(u'documentation_reglementsmunicipaux', 'short_url')

        # Deleting field 'ReglementsMunicipaux.in_sitemap'
        db.delete_column(u'documentation_reglementsmunicipaux', 'in_sitemap')


        # Changing field 'ReglementsMunicipaux.publish_date'
        db.alter_column(u'documentation_reglementsmunicipaux', 'publish_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ReglementsMunicipaux.title'
        db.alter_column(u'documentation_reglementsmunicipaux', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'documentation.avispublics': {
            'Meta': {'object_name': 'AvisPublics', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'})
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
        u'documentation.documentreglementsmunicipaux': {
            'Meta': {'object_name': 'DocumentReglementsMunicipaux'},
            'doctitle': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reglement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'documents'", 'to': u"orm['documentation.ReglementsMunicipaux']"})
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
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'documentation.procesverbauxregietraitement': {
            'Meta': {'object_name': 'ProcesVerbauxRegieTraitement', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'documentation.reglementsmunicipaux': {
            'Meta': {'object_name': 'ReglementsMunicipaux'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['documentation']