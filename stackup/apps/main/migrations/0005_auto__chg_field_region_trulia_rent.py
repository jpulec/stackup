# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Region.trulia_rent'
        db.alter_column(u'main_region', 'trulia_rent', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Region.trulia_rent'
        raise RuntimeError("Cannot reverse this migration. 'Region.trulia_rent' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Region.trulia_rent'
        db.alter_column(u'main_region', 'trulia_rent', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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