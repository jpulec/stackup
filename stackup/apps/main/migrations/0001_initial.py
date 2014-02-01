# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'main_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cl_id', self.gf('django.db.models.fields.IntegerField')()),
            ('cl_rent', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('star_difference', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'main', ['Region'])

        # Adding model 'StandardOfLiving'
        db.create_table(u'main_standardofliving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Region'])),
            ('star_level', self.gf('django.db.models.fields.IntegerField')()),
            ('threshold', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'main', ['StandardOfLiving'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'main_region')

        # Deleting model 'StandardOfLiving'
        db.delete_table(u'main_standardofliving')


    models = {
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            'cl_id': ('django.db.models.fields.IntegerField', [], {}),
            'cl_rent': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'star_difference': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'main.standardofliving': {
            'Meta': {'object_name': 'StandardOfLiving'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Region']"}),
            'star_level': ('django.db.models.fields.IntegerField', [], {}),
            'threshold': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['main']