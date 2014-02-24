# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PurchaseInformation.dealer_purchase_in_charge'
        db.delete_column(u'web_purchaseinformation', 'dealer_purchase_in_charge')

        # Deleting field 'PurchaseInformation.purchaser_sales_man'
        db.delete_column(u'web_purchaseinformation', 'purchaser_sales_man')

        # Deleting field 'PurchaseInformation.dealer_name'
        db.delete_column(u'web_purchaseinformation', 'dealer_name')

        # Deleting field 'PurchaseInformation.invoice_no'
        db.delete_column(u'web_purchaseinformation', 'invoice_no')

        # Deleting field 'PurchaseInformation.contact_person'
        db.delete_column(u'web_purchaseinformation', 'contact_person')

        # Adding field 'PurchaseInformation.delivery_order_number'
        db.add_column(u'web_purchaseinformation', 'delivery_order_number',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PurchaseInformation.dealer_company_name'
        db.add_column(u'web_purchaseinformation', 'dealer_company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PurchaseInformation.dealer_purchaser'
        db.add_column(u'web_purchaseinformation', 'dealer_purchaser',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PurchaseInformation.dealer_sales_man'
        db.add_column(u'web_purchaseinformation', 'dealer_sales_man',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PurchaseInformation.customer'
        db.add_column(u'web_purchaseinformation', 'customer',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PurchaseInformation.dealer_purchase_in_charge'
        raise RuntimeError("Cannot reverse this migration. 'PurchaseInformation.dealer_purchase_in_charge' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PurchaseInformation.purchaser_sales_man'
        raise RuntimeError("Cannot reverse this migration. 'PurchaseInformation.purchaser_sales_man' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PurchaseInformation.dealer_name'
        raise RuntimeError("Cannot reverse this migration. 'PurchaseInformation.dealer_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PurchaseInformation.invoice_no'
        raise RuntimeError("Cannot reverse this migration. 'PurchaseInformation.invoice_no' and its values cannot be restored.")
        # Adding field 'PurchaseInformation.contact_person'
        db.add_column(u'web_purchaseinformation', 'contact_person',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'PurchaseInformation.delivery_order_number'
        db.delete_column(u'web_purchaseinformation', 'delivery_order_number')

        # Deleting field 'PurchaseInformation.dealer_company_name'
        db.delete_column(u'web_purchaseinformation', 'dealer_company_name')

        # Deleting field 'PurchaseInformation.dealer_purchaser'
        db.delete_column(u'web_purchaseinformation', 'dealer_purchaser')

        # Deleting field 'PurchaseInformation.dealer_sales_man'
        db.delete_column(u'web_purchaseinformation', 'dealer_sales_man')

        # Deleting field 'PurchaseInformation.customer'
        db.delete_column(u'web_purchaseinformation', 'customer')

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
            'block_house_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'building_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'dealer_company_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'dealer_po_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dealer_purchaser': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'dealer_sales_man': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'delivery_order_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'delivery_requested_date': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.QuantityDeliveryDate']", 'symmetrical': 'False'}),
            'delivery_requested_date_change': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'delivery_requested_express_delivery': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'extra_man_power_request': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'floor_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'installation_requested_date': ('django.db.models.fields.DateField', [], {}),
            'installation_requested_express_delivery': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'telephone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'unit_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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