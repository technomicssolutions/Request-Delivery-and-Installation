# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dates'
        db.create_table(u'web_dates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Dates'])

        # Adding model 'UserProfile'
        db.create_table(u'web_userprofile', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('brand_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['UserProfile'])

        # Adding model 'SubDealers'
        db.create_table(u'web_subdealers', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('userprofile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['SubDealers'])

        # Adding unique constraint on 'SubDealers', fields ['user', 'userprofile']
        db.create_unique(u'web_subdealers', ['user_id', 'userprofile_id'])

        # Adding model 'QuantityDeliveryDate'
        db.create_table(u'web_quantitydeliverydate', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'web', ['QuantityDeliveryDate'])

        # Adding model 'PurchaseInformation'
        db.create_table(u'web_purchaseinformation', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('slno', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dealer_po_number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dealer_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dealer_purchase_in_charge', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('purchaser_sales_man', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('end_user_delivery_location', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('delivery_requested_express_delivery', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('delivery_requested_date_change', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('installation_requested_date', self.gf('django.db.models.fields.DateField')()),
            ('installation_requested_express_delivery', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('extra_man_power_request', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['PurchaseInformation'])

        # Adding M2M table for field delivery_requested_date on 'PurchaseInformation'
        db.create_table(u'web_purchaseinformation_delivery_requested_date', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('purchaseinformation', models.ForeignKey(orm[u'web.purchaseinformation'], null=False)),
            ('quantitydeliverydate', models.ForeignKey(orm[u'web.quantitydeliverydate'], null=False))
        ))
        db.create_unique(u'web_purchaseinformation_delivery_requested_date', ['purchaseinformation_id', 'quantitydeliverydate_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'SubDealers', fields ['user', 'userprofile']
        db.delete_unique(u'web_subdealers', ['user_id', 'userprofile_id'])

        # Deleting model 'Dates'
        db.delete_table(u'web_dates')

        # Deleting model 'UserProfile'
        db.delete_table(u'web_userprofile')

        # Deleting model 'SubDealers'
        db.delete_table(u'web_subdealers')

        # Deleting model 'QuantityDeliveryDate'
        db.delete_table(u'web_quantitydeliverydate')

        # Deleting model 'PurchaseInformation'
        db.delete_table(u'web_purchaseinformation')

        # Removing M2M table for field delivery_requested_date on 'PurchaseInformation'
        db.delete_table('web_purchaseinformation_delivery_requested_date')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.dates': {
            'Meta': {'object_name': 'Dates'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'web.purchaseinformation': {
            'Meta': {'object_name': 'PurchaseInformation', '_ormbases': [u'web.Dates']},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'dealer_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dealer_po_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dealer_purchase_in_charge': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'delivery_requested_date': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.QuantityDeliveryDate']", 'symmetrical': 'False'}),
            'delivery_requested_date_change': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'delivery_requested_express_delivery': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'end_user_delivery_location': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'extra_man_power_request': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'installation_requested_date': ('django.db.models.fields.DateField', [], {}),
            'installation_requested_express_delivery': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'purchaser_sales_man': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'web.quantitydeliverydate': {
            'Meta': {'object_name': 'QuantityDeliveryDate', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'web.subdealers': {
            'Meta': {'unique_together': "(('user', 'userprofile'),)", 'object_name': 'SubDealers', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': [u'web.Dates']},
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']