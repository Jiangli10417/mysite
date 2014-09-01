# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bill'
        db.create_table(u'Bill', (
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('money', self.gf('django.db.models.fields.IntegerField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('transactor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.User'])),
            ('voucher_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('bill_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('numid', self.gf('django.db.models.fields.IntegerField')()),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'engine', ['Bill'])

        # Adding model 'Account'
        db.create_table(u'Account', (
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project'])),
            ('account_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('money_sum', self.gf('django.db.models.fields.IntegerField')()),
            ('money_act', self.gf('django.db.models.fields.IntegerField')()),
            ('money_lef', self.gf('django.db.models.fields.IntegerField')()),
            ('project_kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Templet'])),
        ))
        db.send_create_signal(u'engine', ['Account'])

        # Adding model 'Templet'
        db.create_table(u'Templet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('temp_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project'])),
            ('device_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('material_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('test_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('fuel_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('trip_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('meeting_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('coperation_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('publish_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('labor_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('other_cost', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'engine', ['Templet'])

        # Adding model 'Project_Category'
        db.create_table(u'Project_Category', (
            ('no', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'engine', ['Project_Category'])

        # Adding model 'Project'
        db.create_table(u'Project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project_Category'])),
            ('pManager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.User'])),
            ('pConntent', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('pStart', self.gf('django.db.models.fields.DateTimeField')()),
            ('pEnd', self.gf('django.db.models.fields.DateTimeField')()),
            ('introDoc', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('userDemanDdoc', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('testScheme', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('iscreate', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'engine', ['Project'])

        # Adding model 'Login'
        db.create_table(u'Login', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('permission', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'engine', ['Login'])

        # Adding model 'User'
        db.create_table(u'User', (
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=9, primary_key=True)),
            ('uname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project'])),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'engine', ['User'])

        # Adding model 'Asset'
        db.create_table(u'Asset', (
            ('asset_id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('asset_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('asset_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Asset_Type'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('manufacture_date', self.gf('django.db.models.fields.DateField')()),
            ('buy_date', self.gf('django.db.models.fields.DateField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('depreciation', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('use_state', self.gf('django.db.models.fields.BooleanField')()),
            ('tid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project'])),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.User'])),
        ))
        db.send_create_signal(u'engine', ['Asset'])

        # Adding model 'Asset_Type'
        db.create_table(u'Asset_Type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('asset_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'engine', ['Asset_Type'])


    def backwards(self, orm):
        # Deleting model 'Bill'
        db.delete_table(u'Bill')

        # Deleting model 'Account'
        db.delete_table(u'Account')

        # Deleting model 'Templet'
        db.delete_table(u'Templet')

        # Deleting model 'Project_Category'
        db.delete_table(u'Project_Category')

        # Deleting model 'Project'
        db.delete_table(u'Project')

        # Deleting model 'Login'
        db.delete_table(u'Login')

        # Deleting model 'User'
        db.delete_table(u'User')

        # Deleting model 'Asset'
        db.delete_table(u'Asset')

        # Deleting model 'Asset_Type'
        db.delete_table(u'Asset_Type')


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
            'numid': ('django.db.models.fields.IntegerField', [], {}),
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