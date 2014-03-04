from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

USER_TYPE_CHOICES = (
    ('customer/dealer' , 'Customer/Dealer'),
    ('sub_dealer', 'Sub Dealer'),
    ('clerk', 'Clerk'),
    ('internal_technician', 'Internal Technician'),
    ('vendors', 'Vendors'),
)

DELIVERED_STATUS = (
    ('pending', 'Pending'),
    ('delivery_confirmed', 'Delivery-Confirmed'),
    ('completed', 'Completed'),
)

INSTALLED_STATUS = (
    ('pending', 'Pending'),
    ('installation_confirmed', 'Installation-Confirmed'),
    ('completed', 'Completed'),
)


class Dates(models.Model):
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True, null=True, blank=True)

class UserProfile(Dates):
    user = models.ForeignKey(User)
    user_type = models.CharField('User Type', null=True, blank=True, max_length=20, choices=USER_TYPE_CHOICES)
    brand_name = models.CharField('Brand', null=True, blank=True, max_length=30)
    dealer_company_name = models.CharField('Dealer/Firm name', null=True, blank=True, max_length=50)
    number_of_failed_login_attempts = models.IntegerField('Failed Login Attempts', default=0)
    login_locked = models.BooleanField('Login is Blocked', default=False)

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

    # def __unicode__(self):
    #     return self.delivery_date
    
    class Meta:
        verbose_name = 'Quantity Delivery Date'
        verbose_name_plural = 'Quantity Delivery Date'

class PurchaseInformation(Dates):
    created_by = models.ForeignKey(User)
    date = models.DateField('Date', null=True, blank=True)
    slno = models.CharField('Sl No', max_length=10, null=True, blank=True)
    dealer_po_number = models.CharField('Dealer PO Number', max_length=30)
    delivery_order_number = models.CharField('Delivery Order Number', max_length=30, null=True, blank=True, unique=True)
    dealer_company_name = models.CharField('Dealer/Company Name', max_length=30, null=True, blank=True)
    dealer_purchaser = models.CharField('Dealer Purchaser', max_length=30, null=True, blank=True)
    dealer_sales_man = models.CharField('Dealer Sales Man', max_length=30, null=True, blank=True)
    brand = models.CharField('Brand', max_length=30)
    model = models.CharField('Model', max_length=30, null=True, blank=True)
    customer = models.CharField('Customer', max_length=50, null=True, blank=True)
    telephone_number = models.CharField('Telephone Number', max_length=15, null=True, blank=True)
    mobile_number = models.CharField('Mobile Number', max_length=15, null=True, blank=True)
    block_house_number = models.CharField('Block/House Number', max_length=10, null=True, blank=True)
    floor_number = models.CharField('Floor Number', max_length=10, null=True, blank=True)
    unit_number = models.CharField('Unit Number', max_length=10, null=True, blank=True)
    building_name = models.CharField('Building Name', max_length=25, null=True, blank=True)
    street_name = models.CharField('Street Name ', max_length=25, null=True, blank=True)
    postal_code = models.CharField('Postal Code', max_length=10, null=True, blank=True)

    delivery_requested_date = models.ManyToManyField(QuantityDeliveryDate)
    delivery_requested_express_delivery = models.TextField('Delivery Requested Express Delivery', max_length=500)
    delivery_requested_date_change = models.IntegerField('Number of changes in Quantity and Delivery Date', default=0)
    delivery_requested_date_change_charge = models.IntegerField('Delivery Requested Date Change Charge', default=0)
    delivery_requested_charge = models.IntegerField('Delivery Requested charge', default=0)
    delivered_status = models.CharField('Delivery Status', null=True, blank=True, max_length=50, choices=DELIVERED_STATUS)
    
    installation_requested_date = models.DateField('Installation Requested Date')
    installation_requested_express_delivery = models.TextField('Installation Requested Express Delivery', max_length=500, null=True, blank=True)
    installation_requested_date_change = models.IntegerField('Number of changes in Installation Requested Date', default=0)
    installation_requested_date_change_charge = models.IntegerField('Installation Requested Date Change Charge', default=0)
    installation_requested_charge = models.IntegerField('Installation Requested charge', default=0)
    installed_status = models.CharField('Installation Status', null=True, blank=True, max_length=50, choices=INSTALLED_STATUS)

    extra_man_power_request = models.IntegerField('Extra Man Power Request', default=0)
    remarks = models.TextField('Remarks', null=True, blank=True)

    def __unicode__(self):
        return self.created_by.first_name

    def get_delivered_status(self):
        try:
            return dict(DELIVERED_STATUS)[self.delivered_status]
        except:
            return 'Pending'

    def get_installed_status(self):
        try:
            return dict(INSTALLED_STATUS)[self.installed_status]
        except:
            return 'Pending'
    
    class Meta:
        verbose_name = 'Purchase Information'
        verbose_name_plural = 'Purchase Information'