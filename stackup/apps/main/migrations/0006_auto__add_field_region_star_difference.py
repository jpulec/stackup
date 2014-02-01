# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Region.star_difference'
        db.add_column(u'main_region', 'star_difference',
                      self.gf('django.db.models.fields.IntegerField')(default=10000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Region.star_difference'
        db.delete_column(u'main_region', 'star_difference')


    models = {
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'star_difference': ('django.db.models.fields.IntegerField', [], {}),
            'trulia_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'trulia_rent': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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