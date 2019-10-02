# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'documentation_document')

        # Deleting model 'Category'
        db.delete_table(u'documentation_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'documentation_subcategory')

        # Adding model 'ProcesVerbauxConseil'
        db.create_table(u'documentation_procesverbauxconseil', (
            (u'basecategory_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseCategory'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['ProcesVerbauxConseil'])

        # Adding model 'BaseDocument'
        db.create_table(u'documentation_basedocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'documentation', ['BaseDocument'])

        # Adding model 'ProcesVerbauxDocument'
        db.create_table(u'documentation_procesverbauxdocument', (
            (u'basedocument_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documentation.BaseDocument'], unique=True, primary_key=True)),
            ('catid', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'procesverbaux', to=orm['documentation.ProcesVerbauxConseil'])),
        ))
        db.send_create_signal(u'documentation', ['ProcesVerbauxDocument'])

        # Adding model 'BaseCategory'
        db.create_table(u'documentation_basecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('s_text', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'documentation', ['BaseCategory'])


    def backwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'documentation_document', (
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'document', to=orm['documentation.Category'])),
            ('sub_category', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'documentation', ['Document'])

        # Adding model 'Category'
        db.create_table(u'documentation_category', (
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
            ('order', self.gf('django.db.models.fields.CharField')(default=u'date', max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('s_text', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'documentation', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'documentation_subcategory', (
            ('title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fk_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentation.Category'])),
        ))
        db.send_create_signal(u'documentation', ['SubCategory'])

        # Deleting model 'ProcesVerbauxConseil'
        db.delete_table(u'documentation_procesverbauxconseil')

        # Deleting model 'BaseDocument'
        db.delete_table(u'documentation_basedocument')

        # Deleting model 'ProcesVerbauxDocument'
        db.delete_table(u'documentation_procesverbauxdocument')

        # Deleting model 'BaseCategory'
        db.delete_table(u'documentation_basecategory')


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
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'BaseDocument'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'})
        },
        u'documentation.procesverbauxconseil': {
            'Meta': {'object_name': 'ProcesVerbauxConseil', '_ormbases': [u'documentation.BaseCategory']},
            u'basecategory_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseCategory']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'documentation.procesverbauxdocument': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ProcesVerbauxDocument', '_ormbases': [u'documentation.BaseDocument']},
            u'basedocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documentation.BaseDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'catid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'procesverbaux'", 'to': u"orm['documentation.ProcesVerbauxConseil']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['documentation']