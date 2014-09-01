# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bill.numid'
        db.delete_column(u'Bill', 'numid')


    def backwards(self, orm):
        # Adding field 'Bill.numid'
        db.add_column(u'Bill', 'numid',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    models = {
        u'engine.account': {
            'Meta': {'object_name': 'Account', 'db_table': "u'Account'"},
            'account_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'money_act': ('django.db.models.fields.IntegerField', [], {}),
            'money_lef': ('django.db.models.fields.IntegerField', [], {}),
            'money_sum': ('django.db.models.fields.IntegerField', [], {}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project']"}),
            'project_kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Templet']"})
        },
        u'engine.asset': {
            'Meta': {'object_name': 'Asset', 'db_table': "u'Asset'"},
            'asset_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'asset_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'asset_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Asset_Type']"}),
            'buy_date': ('django.db.models.fields.DateField', [], {}),
            'depreciation': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'manufacture_date': ('django.db.models.fields.DateField', [], {}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'tid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project']"}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.User']"}),
            'use_state': ('django.db.models.fields.BooleanField', [], {})
        },
        u'engine.asset_type': {
            'Meta': {'object_name': 'Asset_Type', 'db_table': "u'Asset_Type'"},
            'asset_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'engine.bill': {
            'Meta': {'object_name': 'Bill', 'db_table': "u'Bill'"},
            'bill_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'money': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'transactor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.User']"}),
            'voucher_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'engine.login': {
            'Meta': {'object_name': 'Login', 'db_table': "u'Login'"},
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'engine.project': {
            'Meta': {'object_name': 'Project', 'db_table': "u'Project'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introDoc': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'iscreate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project_Category']"}),
            'pConntent': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'pEnd': ('django.db.models.fields.DateTimeField', [], {}),
            'pManager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.User']"}),
            'pName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pStart': ('django.db.models.fields.DateTimeField', [], {}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'testScheme': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'userDemanDdoc': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'engine.project_category': {
            'Meta': {'object_name': 'Project_Category', 'db_table': "u'Project_Category'"},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'engine.templet': {
            'Meta': {'object_name': 'Templet', 'db_table': "u'Templet'"},
            'coperation_cost': ('django.db.models.fields.IntegerField', [], {}),
            'device_cost': ('django.db.models.fields.IntegerField', [], {}),
            'fuel_cost': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labor_cost': ('django.db.models.fields.IntegerField', [], {}),
            'material_cost': ('django.db.models.fields.IntegerField', [], {}),
            'meeting_cost': ('django.db.models.fields.IntegerField', [], {}),
            'other_cost': ('django.db.models.fields.IntegerField', [], {}),
            'publish_cost': ('django.db.models.fields.IntegerField', [], {}),
            'temp_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project']"}),
            'test_cost': ('django.db.models.fields.IntegerField', [], {}),
            'trip_cost': ('django.db.models.fields.IntegerField', [], {})
        },
        u'engine.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'User'"},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project']"}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True'}),
            'uname': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['engine']