# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('questionnaire_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('is_blind', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('questionnaire', ['UserProfile'])

        # Adding model 'Subject'
        db.create_table('questionnaire_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('questionnaire', ['Subject'])

        # Adding model 'QuestionBank'
        db.create_table('questionnaire_questionbank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('questionnaire', ['QuestionBank'])

        # Adding model 'Ques'
        db.create_table('questionnaire_ques', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('ques_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=1)),
            ('ques_bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.QuestionBank'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Subject'])),
        ))
        db.send_create_signal('questionnaire', ['Ques'])

        # Adding model 'Option'
        db.create_table('questionnaire_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Ques'])),
        ))
        db.send_create_signal('questionnaire', ['Option'])

        # Adding model 'Answer'
        db.create_table('questionnaire_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Ques'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Option'])),
        ))
        db.send_create_signal('questionnaire', ['Answer'])

        # Adding model 'Response'
        db.create_table('questionnaire_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Option'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Ques'])),
        ))
        db.send_create_signal('questionnaire', ['Response'])

        # Adding model 'UserScore'
        db.create_table('questionnaire_userscore', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('ques_bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.QuestionBank'])),
            ('score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('questionnaire', ['UserScore'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('questionnaire_userprofile')

        # Deleting model 'Subject'
        db.delete_table('questionnaire_subject')

        # Deleting model 'QuestionBank'
        db.delete_table('questionnaire_questionbank')

        # Deleting model 'Ques'
        db.delete_table('questionnaire_ques')

        # Deleting model 'Option'
        db.delete_table('questionnaire_option')

        # Deleting model 'Answer'
        db.delete_table('questionnaire_answer')

        # Deleting model 'Response'
        db.delete_table('questionnaire_response')

        # Deleting model 'UserScore'
        db.delete_table('questionnaire_userscore')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'questionnaire.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Option']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Ques']"})
        },
        'questionnaire.option': {
            'Meta': {'object_name': 'Option'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Ques']"})
        },
        'questionnaire.ques': {
            'Meta': {'object_name': 'Ques'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ques_bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.QuestionBank']"}),
            'ques_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '1'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Subject']"})
        },
        'questionnaire.questionbank': {
            'Meta': {'object_name': 'QuestionBank'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'questionnaire.response': {
            'Meta': {'object_name': 'Response'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Ques']"}),
            'response': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.Option']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'questionnaire.subject': {
            'Meta': {'object_name': 'Subject'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'questionnaire.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'questionnaire.userscore': {
            'Meta': {'object_name': 'UserScore'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ques_bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['questionnaire.QuestionBank']"}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['questionnaire']