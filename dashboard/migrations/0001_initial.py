# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Container'
        db.create_table(u'dashboard_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['Container'])

        # Adding model 'FeedContainer'
        db.create_table(u'dashboard_feedcontainer', (
            (u'container_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dashboard.Container'], unique=True, primary_key=True)),
            ('external_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('refreshed', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dashboard', ['FeedContainer'])

        # Adding model 'InfoContainer'
        db.create_table(u'dashboard_infocontainer', (
            (u'container_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dashboard.Container'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dashboard', ['InfoContainer'])

        # Adding model 'InfoField'
        db.create_table(u'dashboard_infofield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['dashboard.InfoContainer'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dashboard', ['InfoField'])


    def backwards(self, orm):
        # Deleting model 'Container'
        db.delete_table(u'dashboard_container')

        # Deleting model 'FeedContainer'
        db.delete_table(u'dashboard_feedcontainer')

        # Deleting model 'InfoContainer'
        db.delete_table(u'dashboard_infocontainer')

        # Deleting model 'InfoField'
        db.delete_table(u'dashboard_infofield')


    models = {
        u'dashboard.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.feedcontainer': {
            'Meta': {'object_name': 'FeedContainer', '_ormbases': [u'dashboard.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dashboard.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'refreshed': ('django.db.models.fields.DateTimeField', [], {})
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
        }
    }

    complete_apps = ['dashboard']