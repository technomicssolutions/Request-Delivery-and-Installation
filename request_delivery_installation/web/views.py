# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
import simplejson
from web.models import *
import datetime
from datetime import timedelta


from django.db import IntegrityError


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if user.userprofile_set.all():
            if user.userprofile_set.all()[0].user_type == 'vendors':
                brand = user.userprofile_set.all()[0].brand_name
                current_date = datetime.datetime.now()
                last_two_months = current_date - datetime.timedelta(days=3*30)
                purchase_info = PurchaseInformation.objects.filter(date__gte=last_two_months, brand=brand).order_by('-date')
            elif user.userprofile_set.all()[0].user_type == 'clerk':
                purchase_info = PurchaseInformation.objects.all().order_by('-delivery_requested_date__delivery_date') 
            elif user.userprofile_set.all()[0].user_type == 'internal_technician':
                purchase_info = PurchaseInformation.objects.all().order_by('-installation_requested_date')
            else:
               purchase_info = PurchaseInformation.objects.all().order_by('-created_date') 
        else:
            purchase_info = PurchaseInformation.objects.all()
        if purchase_info:
            context = {
                'purchases': purchase_info,
            }
        return render(request, 'home.html', context)

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html',{})

    def post(self, request, *args, **kwargs):
        
        if not request.is_ajax():
            raise Http404

        status_code = 200
        try:
            post_data = request.POST
            user = authenticate(username=str(post_data['username']), password=post_data['password'])
            if user is not None:
                if user.is_active:
                    if user.is_superuser:
                        login(request, user)
                        res = {'result': 'success', 'message': 'Loged in'}
                    if user.userprofile_set.all(): 
                        userprofile = user.userprofile_set.all()[0]
                        if userprofile.login_locked:
                            res = {
                                'result': 'error',
                                'message': 'More than 3 wrong password attempts, Please contact Admin'
                            }
                        else:
                            userprofile.login_locked = False
                            userprofile.number_of_failed_login_attempts = 0
                            userprofile.save()
                            login(request, user)
                            res = {'result': 'success', 'message': 'Loged in'}
                else:
                    res = {
                        'result': 'error',
                        'message': 'The user is not active',
                    }
                    status_code = 500

                response = simplejson.dumps(res)  
                               
            else:
                status_code = 500
                try:
                    user = User.objects.get(username=str(post_data['username']))
                    if user.userprofile_set.all():
                        userprofile = user.userprofile_set.all()[0]
                        if  userprofile.login_locked:
                            res = {
                                'result':'error',
                                'message':'More than 3 wrong password attempts, Please contact Admin'
                            }
                        else:
                            userprofile.number_of_failed_login_attempts = userprofile.number_of_failed_login_attempts + 1
                            if userprofile.number_of_failed_login_attempts >= 3:
                                userprofile.login_locked = True
                            userprofile.save()
                            res = {
                                'result': 'error',
                                'message': 'Incorrect username and password'
                            }
                except User.DoesNotExist:
                    res = {
                        'result': 'error',
                        'message': 'Incorrect username and password'
                    }
                    
                response = simplejson.dumps(res)
                
        except IntegrityError as ex:
            response = simplejson.dumps({'result': 'error', 'message': 'User with this username doesnot exists '})
            status_code = 500
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class Signup(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'signup.html', {})

    def post(self, request, *args, **kwargs):

        status_code = 200
        try:
            post_dict = request.POST
            user = User.objects.create(first_name=post_dict['firstname'], last_name=post_dict['lastname'],
            email=post_dict['email'], username=post_dict['username'])
            user.set_password(post_dict['password'])
            user.save()
            userprofile = UserProfile.objects.create(user=user, user_type=post_dict['user_type'], brand_name=post_dict['brand'], dealer_company_name=post_dict['dealer_name'] )
            res = {'result': 'success', 'message': 'Loged in'}
        except IntegrityError as ex:
            res = {'result': 'error', 'message': 'User with this username already exists'}
            status_code = 500
        response = simplejson.dumps(res)
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))

class AddSubDealer(View):

    def get(self, request, *args, **kwargs):
        context = {}
        user = User.objects.get(id = kwargs['user_id'])
        sub_dealers = SubDealers.objects.filter(userprofile = user.userprofile_set.all()[0]).count()
        if sub_dealers >= 20:
            context = {
                'message': 'You have already Added 20 subdealers',
            }

        return render(request, 'add_subdealer.html', context)

    def post(self, request, *args, **kwargs):
        post_dict = request.POST
        status_code = 200
        try: 
            dealer = UserProfile.objects.get(user_id = kwargs['user_id'])
            user = User.objects.create(first_name=post_dict['firstname'], last_name=post_dict['lastname'],
            email=post_dict['email'], username=post_dict['email'])
            user.set_password(post_dict['password'])
            user.save()
            userprofile = UserProfile.objects.create(user=user, user_type=post_dict['user_type'])
            subdealer = SubDealers.objects.create(user=user, userprofile=dealer)
            response = simplejson.dumps({'result': 'success', 'message': 'Added Successfully'})
        except IntegrityError as ex:
            response = simplejson.dumps({'result': 'error', 'message': 'User with this username already exists'})
            status_code = 500
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class AddPurchanseInfo(View):
    def get(self, request, *args, **kwargs):

        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        purchase_date = current_date.strftime('%d-%m-%Y')
        context = {
            'date': purchase_date,
        }
        return render(request, 'add_purchase_info.html', context)

    def post(self, request, *args, **kwargs):

        post_dict = request.POST
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        try:
            status_code = 200
            purchases = PurchaseInformation.objects.all().count()
            if int(purchases) > 0:
                latest_purchase = PurchaseInformation.objects.latest('id')
                sl_no = int(latest_purchase.slno) + 1
            else:
                sl_no = 1
            purchase_info = PurchaseInformation()
            purchase_info.created_by = request.user
            day, month, year = post_dict['date'].split('-')
            purchase_date = datetime.date(int(year), int(month), int(day))
            purchase_info.date = purchase_date
            purchase_info.slno = sl_no
            purchase_info.dealer_po_number = post_dict['dealer_po_number']
            purchase_info.delivery_order_number = post_dict['delivery_order_number']
            purchase_info.dealer_company_name = post_dict['dealer_company_name']
            purchase_info.dealer_purchaser = post_dict['dealer_purchaser']
            purchase_info.dealer_sales_man = post_dict['dealer_sales_man']
            purchase_info.brand = post_dict['brand']
            purchase_info.model = post_dict['model']
            purchase_info.customer = post_dict['customer']
            purchase_info.block_house_number = post_dict['block_house_no']
            purchase_info.floor_number = post_dict['floor_no']
            purchase_info.unit_number = post_dict['unit_no']
            purchase_info.building_name = post_dict['building_name']
            purchase_info.street_name = post_dict['street_name']
            purchase_info.postal_code = post_dict['postal_code']
            purchase_info.telephone_number = post_dict['telephone_no']
            purchase_info.mobile_number = post_dict['mobile_no']
            # purchase_info.installation_requested_date = post_dict['installation_requested_date']
            purchase_info.extra_man_power_request = post_dict['extra_man_power']
            purchase_info.delivered_status = 'pending'
            purchase_info.installed_status = 'pending'
            purchase_info.remarks = post_dict['remarks']
            
            day, month, year = post_dict['installation_requested_date'].split('-')
            installation_requested_date = datetime.date(int(year), int(month), int(day))
            if current_date == installation_requested_date:
                if current_time.hour >= 12:
                    next_date = (datetime.datetime.now() + timedelta(days = 1)).date()
                    if next_date.strftime("%A") == 'Sunday':
                        next_date = next_date + timedelta(days = 1)
                        installation_requested_date = next_date
                    elif next_date.strftime("%A") == 'Saturday':
                        next_date = next_date + timedelta(days = 2)
                        installation_requested_date = next_date
                    else:
                        installation_requested_date = next_date
                else:
                    installation_requested_date = datetime.date(int(year), int(month), int(day))
            purchase_info.installation_requested_date = installation_requested_date 
            installation_date_diff = (installation_requested_date - purchase_date).days
            if installation_date_diff < 3:
                purchase_info.installation_requested_express_delivery = 'Express delivery'
            if installation_date_diff == 0:
                purchase_info.installation_requested_charge = 400
            elif installation_date_diff == 1:
                purchase_info.installation_requested_charge = 200
            elif installation_date_diff == 2:
                purchase_info.installation_requested_charge = 100
            else:
                purchase_info.installation_requested_charge = 0
            purchase_info.installation_requested_date_change_charge = int(purchase_info.installation_requested_date_change) * 30

            purchase_info.save()
            
            day, month, year = post_dict['delivery_requested_date'].split('-')
            delivery_requested_date = datetime.date(int(year), int(month), int(day))
            if current_date == delivery_requested_date:
                if current_time.hour >= 12:
                    next_date = (datetime.datetime.now() + timedelta(days = 1)).date()
                    if next_date.strftime("%A") == 'Sunday':
                        next_date = next_date + timedelta(days = 1)
                        delivery_requested_date = next_date
                    elif next_date.strftime("%A") == 'Saturday':
                        next_date = next_date + timedelta(days = 2)
                        delivery_requested_date = next_date
                    else:
                        delivery_requested_date = next_date
                else:
                    delivery_requested_date = datetime.date(int(year), int(month), int(day))
            quantity_delivery_date = QuantityDeliveryDate.objects.create(quantity= post_dict['quantity'], delivery_date=delivery_requested_date)
            purchase_info.delivery_requested_date.add(quantity_delivery_date) 
            purchase_info.save()
            
            for delivery_details in purchase_info.delivery_requested_date.all():
                delivery_date = delivery_details.delivery_date
                delivery_date_diff = (delivery_date - purchase_date).days
            if delivery_date_diff < 3:
                purchase_info.delivery_requested_express_delivery = 'Express delivery'
            if delivery_date_diff == 0:
                purchase_info.delivery_requested_charge = 400
            elif delivery_date_diff == 1:
                purchase_info.delivery_requested_charge = 200
            elif delivery_date_diff == 2:
                purchase_info.delivery_requested_charge = 100
            else:
                purchase_info.delivery_requested_charge = 0
            purchase_info.delivery_requested_date_change_charge = int(purchase_info.delivery_requested_date_change) * 30

            purchase_info.save()
            response = simplejson.dumps({'result': 'success', 'message': 'Successfully added'})
        except IntegrityError as ex:
            response = simplejson.dumps({'result': 'error', 'message': 'Duplicate Entry for the Delivery Order Number'})
            status_code = 500
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class FetchBrandNames(View):
    def get(self, request, *args, **kwargs):
        ctx_brands = []
        brands =  PurchaseInformation.objects.all().values_list('brand', flat = True).distinct()
        if brands.count() > 0:
            for brand in brands:
                ctx_brands.append({
                   'brand_name': brand
                })
        response = simplejson.dumps({'result': 'sucess', 'brands': ctx_brands})
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class FetchPurchaseSalesManList(View):
    def get(self, request, *args, **kwargs):
        ctx_dealer_sales_men = []
        dealer_sales_men =  PurchaseInformation.objects.all().values_list('dealer_sales_man', flat = True).distinct()
        if dealer_sales_men.count() > 0:
            for dealer_sales_man in dealer_sales_men:
                ctx_dealer_sales_men.append({
                   'name': dealer_sales_man
                })
        response = simplejson.dumps({'result': 'sucess', 'purchase_sales_men': ctx_dealer_sales_men})
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class FetchDealersList(View):
    def get(self, request, *args, **kwargs):
        ctx_dealers = []
        dealers =  PurchaseInformation.objects.all().values_list('dealer_purchaser', flat = True).distinct()
        if dealers.count() > 0:
            for dealer in dealers:
                ctx_dealers.append({
                   'name': dealer
                })
        response = simplejson.dumps({'result': 'sucess', 'dealers': ctx_dealers})
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype = 'application/json')


class PurchaseInfoView(View):

    def get(self, request, *args, **kwargs):

        purchase_info = PurchaseInformation.objects.get(id=kwargs['purchase_info_id'])
        purchase_info.date = purchase_info.date.strftime('%d-%m-%Y')
        current_date = datetime.datetime.now().date()
        delivered_status = False
        installed_status = False
        pending = False
        confirmed = False
        not_delivered = False
        not_confirmed = False
        not_pending = False
        for purchase_detail in purchase_info.delivery_requested_date.all():
            delivery_date = purchase_detail.delivery_date
        user = request.user
        if user.is_superuser:
            installed_status = True
            delivered_status = True
            
        if user.userprofile_set.all():
            if user.userprofile_set.all()[0].user_type == 'clerk':
                delivered_status = True
                if purchase_info.delivered_status == 'pending':
                    pending = True
                elif purchase_info.delivered_status == 'delivery_confirmed':
                    confirmed = True
            elif user.userprofile_set.all()[0].user_type == 'internal_technician':
                installed_status = True

                if purchase_info.delivered_status == 'completed' and purchase_info.installed_status == 'pending':
                    pending = True
                
                elif purchase_info.delivered_status == 'completed' and purchase_info.installed_status == 'installation_confirmed':
                    not_pending = True
                
                elif purchase_info.delivered_status == 'delivery_confirmed' and purchase_info.installed_status == 'installation_confirmed':
                    confirmed = True
                
                elif purchase_info.delivered_status == 'delivery_confirmed' and purchase_info.installed_status == 'pending':
                    not_delivered = True
                
                elif purchase_info.delivered_status == 'pending':
                    not_confirmed = True
                    
                # elif purchase_info.installed_status == 'installation_confirmed' and purchase_info.delivered_status != 'completed':
                #     not_delivered = True
        purchase_info.installation_requested_date = purchase_info.installation_requested_date.strftime('%d-%m-%Y')
        context = {
            'purchase': purchase_info,
            'delivery_status': delivered_status,
            'installed_status': installed_status,
            'pending': pending,
            'confirmed': confirmed,
            'not_delivered': not_delivered,
            'not_confirmed': not_confirmed,
            'not_pending': not_pending
        }
        return render(request, 'view_purchase_info.html', context)

    def post(self, request, *args, **kwargs):

        post_dict = request.POST
        changed_quantity = False
        changed_delivery_date = False
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        
        purchase_info = PurchaseInformation.objects.get(id=kwargs['purchase_info_id'])
        # try:
        user = request.user

        purchase_info.delivery_order_number = post_dict['delivery_order_number']
        purchase_info.dealer_sales_man = post_dict['dealer_sales_man']
        purchase_info.brand = post_dict['brand']
        purchase_info.model = post_dict['model']
        purchase_info.customer = post_dict['customer']
        purchase_info.block_house_number = post_dict['block_house_no']
        purchase_info.floor_number = post_dict['floor_no']
        purchase_info.unit_number = post_dict['unit_no']
        purchase_info.building_name = post_dict['building_name']
        purchase_info.street_name = post_dict['street_name']
        purchase_info.postal_code = post_dict['postal_code']
        purchase_info.telephone_number = post_dict['telephone_no']
        purchase_info.mobile_number = post_dict['mobile_no']
        purchase_info.remarks = post_dict['remarks']

        purchase_info.dealer_po_number = post_dict['dealer_po_number']
        purchase_info.dealer_company_name = post_dict['dealer_company_name']
        purchase_info.dealer_purchaser = post_dict['dealer_purchaser']
                       
        purchase_info.extra_man_power_request = post_dict['extra_man_power_request']
        purchase_info.delivered_status = post_dict['delivery_status']
        purchase_info.installed_status = post_dict['installed_status']
        quantity = ''
        delivery_date = ''

        purchase_date = purchase_info.date
        
        for purchase_detail in purchase_info.delivery_requested_date.all():
            quantity = purchase_detail.quantity
            delivery_date = purchase_detail.delivery_date
        
        if quantity != post_dict['quantity']:
            quantity = post_dict['quantity']
            changed_quantity = True

        day, month, year = post_dict['delivery_requested_date'].split('-')
        new_delivery_requested_date = datetime.date(int(year), int(month), int(day))
        if delivery_date != new_delivery_requested_date:
            delivery_date = new_delivery_requested_date
            changed_delivery_date = True
        
        if changed_delivery_date or changed_quantity:
            quantity_delivery_date = QuantityDeliveryDate.objects.create(quantity= quantity, delivery_date=new_delivery_requested_date)
            
            # year, month, day = quantity_delivery_date.delivery_date.split('-')
            # delivery_date = datetime.date(int(year), int(month), int(day))

            delivery_date = quantity_delivery_date.delivery_date
            if current_date == delivery_date:
                if current_time.hour >= 12:
                    next_date = (datetime.datetime.now() + timedelta(days = 1)).date()
                    if next_date.strftime("%A") == 'Sunday':
                        next_date = next_date + timedelta(days = 1)
                        delivery_date = next_date
                    elif next_date.strftime("%A") == 'Saturday':
                        next_date = next_date + timedelta(days = 2)
                        delivery_date = next_date
                    else:
                        delivery_date = next_date
                else:
                    delivery_date = datetime.date(int(year), int(month), int(day))

            delivery_date_diff = (delivery_date - purchase_date).days
            if delivery_date_diff < 3:
                purchase_info.delivery_requested_express_delivery = 'Express delivery'
                purchase_info.save()
            else:
                purchase_info.delivery_requested_express_delivery = ''
            purchase_info.delivery_requested_date.clear()
            purchase_info.delivery_requested_date.add(quantity_delivery_date)
            
            if changed_delivery_date:
                purchase_info.delivery_requested_date_change = purchase_info.delivery_requested_date_change + 1
            
                if delivery_date_diff == 0:
                    purchase_info.delivery_requested_charge = 400
                elif delivery_date_diff == 1:
                    purchase_info.delivery_requested_charge = 200
                elif delivery_date_diff == 2:
                    purchase_info.delivery_requested_charge = 100
                else:
                    purchase_info.delivery_requested_charge = 0
                
                purchase_info.delivery_requested_date_change_charge = int(purchase_info.delivery_requested_date_change) * 30
            purchase_info.save()
        else:
            purchase_info.delivery_requested_express_delivery = purchase_info.delivery_requested_express_delivery
            purchase_info.save()

        day, month, year = post_dict['installation_requested_date'].split('-')
        installation_requested_date = datetime.date(int(year), int(month), int(day))
        if purchase_info.installation_requested_date != installation_requested_date:
            purchase_info.installation_requested_date_change = purchase_info.installation_requested_date_change + 1

            if current_date == installation_requested_date:
                if current_time.hour >= 12:
                    next_date = (datetime.datetime.now() + timedelta(days = 1)).date()
                    if next_date.strftime("%A") == 'Sunday':
                        next_date = next_date + timedelta(days = 1)
                        installation_requested_date = next_date
                    elif next_date.strftime("%A") == 'Saturday':
                        next_date = next_date + timedelta(days = 2)
                        installation_requested_date = next_date
                    else:
                        installation_requested_date = next_date
                else:
                    installation_requested_date = datetime.date(int(year), int(month), int(day))

            installation_date_diff = (installation_requested_date - purchase_date).days
            if installation_date_diff < 3:
                purchase_info.installation_requested_express_delivery = 'Express delivery'
            else:
                purchase_info.installation_requested_express_delivery = ''
            if installation_date_diff == 0:
                purchase_info.installation_requested_charge = 400
            elif installation_date_diff == 1:
                purchase_info.installation_requested_charge = 200
            elif installation_date_diff == 2:
                purchase_info.installation_requested_charge = 100
            else:
                purchase_info.installation_requested_charge = 0
            purchase_info.installation_requested_date_change_charge = int(purchase_info.installation_requested_date_change) * 30
            purchase_info.installation_requested_date = installation_requested_date
            purchase_info.save() 
        else:
            purchase_info.installation_requested_express_delivery = purchase_info.installation_requested_express_delivery
            purchase_info.save()
            # purchase_info.installation_requested_date = purchase_info.installation_requested_date.strftime('%Y-%m-%j') 
        context = {'result': 'success', 'message': 'Edited Successfully', 'purchase': purchase_info,}    
        # except Exception as ex:
        #     print str(ex)
        #     context = {'result': 'error', 'message': str(ex), 'purchase': purchase_info,}
        
        return render(request,'view_purchase_info.html', context)

class SearchPurchaseInfo(View):

    def get(self, request, *args, **kwargs):

        try:
            purchase_info = PurchaseInformation.objects.get(delivery_order_number=kwargs['delivery_order_number'])
            purchase_info.date = purchase_info.date.strftime('%Y-%m-%d')
            purchase_info.installation_requested_date = purchase_info.installation_requested_date.strftime('%Y-%m-%d')
            current_date = datetime.datetime.now().date()
            delivered_status = False
            for purchase_detail in purchase_info.delivery_requested_date.all():
                delivery_date = purchase_detail.delivery_date
            if current_date >= delivery_date:
                delivered_status = True
            else:
                delivered_status = False

        except PurchaseInformation.DoesNotExist:
            purchase_info = None
            message = 'No Purchase Information with this Delivery Order Number is Available'
            context = {
                'message': message
            }
            return render(request, 'home.html', context)
        context = {
            'purchase': purchase_info,
            'delivery_status': delivered_status
        }
        return render(request, 'view_purchase_info.html', context)

class FetchFirmNames(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        ctx_dealers = []
        if user.userprofile_set.all():
            if user.userprofile_set.all()[0].user_type == 'customer/dealer':
                response = simplejson.dumps({'result': 'sucess', 'dealer_company_names': user.userprofile_set.all()[0].dealer_company_name, 'is_dealer':True})
                status_code = 200
                return HttpResponse(response, status = status_code, mimetype = 'application/json')
            else:
                dealer_company_names =  PurchaseInformation.objects.all().values_list('dealer_company_name', flat = True).distinct()
                if dealer_company_names.count() > 0:
                    for dealer in dealer_company_names:
                        ctx_dealers.append({
                           'name': dealer
                        })
        else:
            dealer_company_names =  PurchaseInformation.objects.all().values_list('dealer_company_name', flat = True).distinct()
            if dealer_company_names.count() > 0:
                for dealer in dealer_company_names:
                    ctx_dealers.append({
                       'name': dealer
                    })

        response = simplejson.dumps({'result': 'sucess', 'dealer_company_names': ctx_dealers, 'is_dealer':False})
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype = 'application/json')




        







