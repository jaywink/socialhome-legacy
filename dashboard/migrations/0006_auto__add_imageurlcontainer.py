# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageURLContainer'
        db.create_table(u'dashboard_imageurlcontainer', (
            (u'container_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dashboard.Container'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'dashboard', ['ImageURLContainer'])


    def backwards(self, orm):
        # Deleting model 'ImageURLContainer'
        db.delete_table(u'dashboard_imageurlcontainer')


    models = {
        u'dashboard.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'})
        },
        u'dashboard.feedcontainer': {
            'Meta': {'object_name': 'FeedContainer', '_ormbases': [u'dashboard.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'refreshed': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'dashboard.iframecontainer': {
            'Meta': {'object_name': 'IFrameContainer', '_ormbases': [u'dashboard.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dashboard.imageurlcontainer': {
            'Meta': {'object_name': 'ImageURLContainer', '_ormbases': [u'dashboard.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dashboard.infocontainer': {
            'Meta': {'object_name': 'InfoContainer', '_ormbases': [u'dashboard.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dashboard.infofield': {
            'Meta': {'object_name': 'InfoField'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['dashboard.InfoContainer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'dashboard.widgetcontainer': {
            'Meta': {'object_name': 'WidgetContainer', '_ormbases': [u'dashboard.Container']},
            'code': ('django.db.models.fields.TextField', [], {}),
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'include_libs': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dashboard']