# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Geocode'
        db.create_table(u'main_geocode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'main', ['Geocode'])


    def backwards(self, orm):
        # Deleting model 'Geocode'
        db.delete_table(u'main_geocode')


    models = {
        u'main.geocode': {
            'Meta': {'object_name': 'Geocode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            'cl_id': ('django.db.models.fields.IntegerField', [], {}),
            'cl_rent': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'crime_score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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