from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
USER_TYPE_CHOICES = (
    ('customer/dealer' , 'Customer/Dealer'),
    ('sub_dealer', 'Sub Dealer'),
    ('sales_executive', 'Sales Executive'),
    ('internal_technician', 'Internal Technician'),
    ('vendors', 'Vendors'),
)

class Dates(models.Model):
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True, null=True, blank=True)

class UserProfile(Dates):
    user = models.ForeignKey(User)
    user_type = models.CharField('User Type', null=True, blank=True, max_length=20, choices=USER_TYPE_CHOICES)
    brand_name = models.CharField('Brand', null=True, blank=True, max_length=30)

    def get_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        else:
            return self.user.username

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'
        
class SubDealers(Dates):

    user = models.ForeignKey(User)
    userprofile = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    class Meta:
        verbose_name = 'Sub Dealers'
        verbose_name_plural = 'Sub Dealers'
        unique_together = ('user', 'userprofile')

class QuantityDeliveryDate(Dates):
    quantity = models.IntegerField('Quantity', default=0)
    delivery_date = models.DateField('Delivery Date')

    def __unicode__(self):
        return self.delivery_date
    
    class Meta:
        verbose_name = 'Quantity Delivery Date'
        verbose_name_plural = 'Quantity Delivery Date'

class PurchaseInformation(Dates):
    created_by = models.ForeignKey(User)
    date = models.DateField('Date', null=True, blank=True)
    slno = models.CharField('Sl No', max_length=10, null=True, blank=True)
    dealer_po_number = models.CharField('Dealer PO Number', max_length=30)
    dealer_name = models.CharField('Dealer Name', max_length=30)
    dealer_purchase_in_charge = models.CharField('Name of Dealer Purchaser-In-Charge', max_length=30)
    purchaser_sales_man = models.CharField('Purchaser Sales Man', max_length=30)
    brand = models.CharField('Brand', max_length=30)
    model = models.CharField('Model', max_length=30, null=True, blank=True)
    address = models.TextField('Address', max_length=500, null=True, blank=True)
    contact_person = models.CharField('Contact Person', max_length=50, null=True, blank=True)
    contact_number = models.CharField('Contact Number', max_length=15, null=True, blank=True)
    delivery_requested_date = models.ManyToManyField(QuantityDeliveryDate)
    delivery_requested_express_delivery = models.TextField('Delivery Requested Express Delivery', max_length=500)
    delivery_requested_date_change = models.IntegerField('Number of changes in Quantity and Delivery Date', default=0)
    installation_requested_date = models.DateField('Installation Requested Date')
    installation_requested_express_delivery = models.TextField('Installation Requested Express Delivery', max_length=500)
    extra_man_power_request = models.IntegerField('Extra Man Power Request', default=0)
    remarks = models.TextField('Remarks', null=True, blank=True)

    def __unicode__(self):
        return self.created_by.first_name
    
    class Meta:
        verbose_name = 'Purchase Information'
        verbose_name_plural = 'Purchase Information'
