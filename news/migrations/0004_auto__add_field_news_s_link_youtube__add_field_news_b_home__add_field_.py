# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.s_link_youtube'
        db.add_column(u'news_news', 's_link_youtube',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.b_home'
        db.add_column(u'news_news', 'b_home',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'News.ik_home_image'
        db.add_column(u'news_news', 'ik_home_image',
                      self.gf('mezzanine.core.fields.FileField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.s_excerpt_home'
        db.add_column(u'news_news', 's_excerpt_home',
                      self.gf('django.db.models.fields.TextField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'News.s_link_title'
        db.alter_column(u'news_news', 's_link_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'News.s_link'
        db.alter_column(u'news_news', 's_link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'News.ik_diapo'
        db.alter_column(u'news_news', 'ik_diapo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galleries.Gallery'], null=True))

    def backwards(self, orm):
        # Deleting field 'News.s_link_youtube'
        db.delete_column(u'news_news', 's_link_youtube')

        # Deleting field 'News.b_home'
        db.delete_column(u'news_news', 'b_home')

        # Deleting field 'News.ik_home_image'
        db.delete_column(u'news_news', 'ik_home_image')

        # Deleting field 'News.s_excerpt_home'
        db.delete_column(u'news_news', 's_excerpt_home')


        # Changing field 'News.s_link_title'
        db.alter_column(u'news_news', 's_link_title', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'News.s_link'
        db.alter_column(u'news_news', 's_link', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'News.ik_diapo'
        db.alter_column(u'news_news', 'ik_diapo_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['galleries.Gallery']))

    models = {
        u'galleries.gallery': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Gallery', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'zip_import': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'b_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dt_begin': ('django.db.models.fields.DateField', [], {}),
            'dt_end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ik_diapo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['galleries.Gallery']", 'null': 'True', 'blank': 'True'}),
            'ik_home_image': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ik_image': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            's_excerpt_home': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            's_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            's_link_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            's_link_youtube': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            's_text': ('django.db.models.fields.TextField', [], {}),
            's_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['news']