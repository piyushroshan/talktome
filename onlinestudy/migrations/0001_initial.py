# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('onlinestudy_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('onlinestudy', ['Subject'])

        # Adding model 'Topic'
        db.create_table('onlinestudy_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlinestudy.Subject'])),
        ))
        db.send_create_signal('onlinestudy', ['Topic'])

        # Adding model 'Material'
        db.create_table('onlinestudy_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('upFile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlinestudy.Topic'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlinestudy.Subject'])),
        ))
        db.send_create_signal('onlinestudy', ['Material'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('onlinestudy_subject')

        # Deleting model 'Topic'
        db.delete_table('onlinestudy_topic')

        # Deleting model 'Material'
        db.delete_table('onlinestudy_material')


    models = {
        'onlinestudy.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['onlinestudy.Subject']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['onlinestudy.Topic']"}),
            'upFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'onlinestudy.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'onlinestudy.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['onlinestudy.Subject']"})
        }
    }

    complete_apps = ['onlinestudy']