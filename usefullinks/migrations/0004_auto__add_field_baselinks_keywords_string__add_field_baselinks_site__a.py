# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseLinks.keywords_string'
        db.add_column(u'usefullinks_baselinks', u'keywords_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.site'
        db.add_column(u'usefullinks_baselinks', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'BaseLinks.title'
        db.add_column(u'usefullinks_baselinks', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Titre', max_length=500),
                      keep_default=False)

        # Adding field 'BaseLinks.slug'
        db.add_column(u'usefullinks_baselinks', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks._meta_title'
        db.add_column(u'usefullinks_baselinks', '_meta_title',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.description'
        db.add_column(u'usefullinks_baselinks', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.gen_description'
        db.add_column(u'usefullinks_baselinks', 'gen_description',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'BaseLinks.created'
        db.add_column(u'usefullinks_baselinks', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'BaseLinks.updated'
        db.add_column(u'usefullinks_baselinks', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'BaseLinks.status'
        db.add_column(u'usefullinks_baselinks', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'BaseLinks.publish_date'
        db.add_column(u'usefullinks_baselinks', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.expiry_date'
        db.add_column(u'usefullinks_baselinks', 'expiry_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.short_url'
        db.add_column(u'usefullinks_baselinks', 'short_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseLinks.in_sitemap'
        db.add_column(u'usefullinks_baselinks', 'in_sitemap',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'RepertoryLinks.short_url'
        db.delete_column(u'usefullinks_repertorylinks', 'short_url')

        # Deleting field 'RepertoryLinks.site'
        db.delete_column(u'usefullinks_repertorylinks', 'site_id')

        # Deleting field 'RepertoryLinks.keywords_string'
        db.delete_column(u'usefullinks_repertorylinks', u'keywords_string')

        # Deleting field 'RepertoryLinks.in_sitemap'
        db.delete_column(u'usefullinks_repertorylinks', 'in_sitemap')

        # Deleting field 'RepertoryLinks.title'
        db.delete_column(u'usefullinks_repertorylinks', 'title')

        # Deleting field 'RepertoryLinks.status'
        db.delete_column(u'usefullinks_repertorylinks', 'status')

        # Deleting field 'RepertoryLinks.updated'
        db.delete_column(u'usefullinks_repertorylinks', 'updated')

        # Deleting field 'RepertoryLinks.description'
        db.delete_column(u'usefullinks_repertorylinks', 'description')

        # Deleting field 'RepertoryLinks.expiry_date'
        db.delete_column(u'usefullinks_repertorylinks', 'expiry_date')

        # Deleting field 'RepertoryLinks.slug'
        db.delete_column(u'usefullinks_repertorylinks', 'slug')

        # Deleting field 'RepertoryLinks.gen_description'
        db.delete_column(u'usefullinks_repertorylinks', 'gen_description')

        # Deleting field 'RepertoryLinks.created'
        db.delete_column(u'usefullinks_repertorylinks', 'created')

        # Deleting field 'RepertoryLinks._meta_title'
        db.delete_column(u'usefullinks_repertorylinks', '_meta_title')

        # Deleting field 'RepertoryLinks.publish_date'
        db.delete_column(u'usefullinks_repertorylinks', 'publish_date')


    def backwards(self, orm):
        # Deleting field 'BaseLinks.keywords_string'
        db.delete_column(u'usefullinks_baselinks', u'keywords_string')

        # Deleting field 'BaseLinks.site'
        db.delete_column(u'usefullinks_baselinks', 'site_id')

        # Deleting field 'BaseLinks.title'
        db.delete_column(u'usefullinks_baselinks', 'title')

        # Deleting field 'BaseLinks.slug'
        db.delete_column(u'usefullinks_baselinks', 'slug')

        # Deleting field 'BaseLinks._meta_title'
        db.delete_column(u'usefullinks_baselinks', '_meta_title')

        # Deleting field 'BaseLinks.description'
        db.delete_column(u'usefullinks_baselinks', 'description')

        # Deleting field 'BaseLinks.gen_description'
        db.delete_column(u'usefullinks_baselinks', 'gen_description')

        # Deleting field 'BaseLinks.created'
        db.delete_column(u'usefullinks_baselinks', 'created')

        # Deleting field 'BaseLinks.updated'
        db.delete_column(u'usefullinks_baselinks', 'updated')

        # Deleting field 'BaseLinks.status'
        db.delete_column(u'usefullinks_baselinks', 'status')

        # Deleting field 'BaseLinks.publish_date'
        db.delete_column(u'usefullinks_baselinks', 'publish_date')

        # Deleting field 'BaseLinks.expiry_date'
        db.delete_column(u'usefullinks_baselinks', 'expiry_date')

        # Deleting field 'BaseLinks.short_url'
        db.delete_column(u'usefullinks_baselinks', 'short_url')

        # Deleting field 'BaseLinks.in_sitemap'
        db.delete_column(u'usefullinks_baselinks', 'in_sitemap')

        # Adding field 'RepertoryLinks.short_url'
        db.add_column(u'usefullinks_repertorylinks', 'short_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.site'
        db.add_column(u'usefullinks_repertorylinks', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'RepertoryLinks.keywords_string'
        db.add_column(u'usefullinks_repertorylinks', u'keywords_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.in_sitemap'
        db.add_column(u'usefullinks_repertorylinks', 'in_sitemap',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.title'
        db.add_column(u'usefullinks_repertorylinks', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Titre', max_length=500),
                      keep_default=False)

        # Adding field 'RepertoryLinks.status'
        db.add_column(u'usefullinks_repertorylinks', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'RepertoryLinks.updated'
        db.add_column(u'usefullinks_repertorylinks', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.description'
        db.add_column(u'usefullinks_repertorylinks', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.expiry_date'
        db.add_column(u'usefullinks_repertorylinks', 'expiry_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.slug'
        db.add_column(u'usefullinks_repertorylinks', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.gen_description'
        db.add_column(u'usefullinks_repertorylinks', 'gen_description',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.created'
        db.add_column(u'usefullinks_repertorylinks', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks._meta_title'
        db.add_column(u'usefullinks_repertorylinks', '_meta_title',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'RepertoryLinks.publish_date'
        db.add_column(u'usefullinks_repertorylinks', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


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
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'linktitle': ('django.db.models.fields.CharField', [], {'default': "u'Titre'", 'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'usefullinks.repertorylinks': {
            'Meta': {'object_name': 'RepertoryLinks', '_ormbases': [u'usefullinks.BaseLinks']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'baselinks_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['usefullinks.BaseLinks']", 'unique': 'True', 'primary_key': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contactname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'excerpt': ('mezzanine.core.fields.RichTextField', [], {'default': "u'R\\xe9sum\\xe9'"}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ik_image': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'repertory_category': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'usefullink_category': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'usefullinks.usefullinks': {
            'Meta': {'object_name': 'UsefulLinks', '_ormbases': [u'usefullinks.BaseLinks']},
            u'baselinks_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['usefullinks.BaseLinks']", 'unique': 'True', 'primary_key': 'True'}),
            'categorie': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['usefullinks']