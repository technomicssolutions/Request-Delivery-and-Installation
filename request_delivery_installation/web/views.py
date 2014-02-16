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


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if user.userprofile_set.all()[0].user_type == 'vendors':
            current_date = datetime.datetime.now()
            last_two_months = current_date - datetime.timedelta(days=3*30)
            purchase_info = PurchaseInformation.objects.filter(date__gte=last_two_months)
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
                    login(request, user)
                    res = {'result': 'success', 'message': 'Loged in'}
                else:
                    res = {
                        'result': 'error',
                        'error_value': 'The user is not active',
                    }
                    status_code = 500

                response = simplejson.dumps(res)  
                               
            else:
                response = simplejson.dumps({'result': 'error', 'message': 'Incorrect username and password'})
                status_code = 500
                
        except Exception as ex:
            response = simplejson.dumps({'result': 'error', 'message': str(ex)})
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
            email=post_dict['email'], username=post_dict['email'])
            user.set_password(post_dict['password'])
            user.save()
            userprofile = UserProfile.objects.create(user=user, user_type=post_dict['user_type'], brand_name=post_dict['brand'] )
            res = {'result': 'success', 'message': 'Loged in'}
        except Exception as ex:
            res = {'result': 'error', 'message': str(ex)}
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
        if sub_dealers > 20:
            context = {
                'message': 'You have already 20 subdealers',
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
        except Exception as ex:
            response = simplejson.dumps({'result': 'error', 'message': str(ex)})
            status_code = 500
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class AddPurchanseInfo(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'add_purchase_info.html', {})

    def post(self, request, *args, **kwargs):
        post_dict = request.POST
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
            purchase_info.date = post_dict['date']
            purchase_info.slno = sl_no
            purchase_info.dealer_po_number = post_dict['dealer_po_number']
            purchase_info.invoice_no = post_dict['invoice_no']
            purchase_info.dealer_name = post_dict['dealer_name']
            purchase_info.dealer_purchase_in_charge = post_dict['dealer_purchase_in_charge']
            purchase_info.purchaser_sales_man = post_dict['purchaser_sales_man']
            purchase_info.brand = post_dict['brand']
            purchase_info.model = post_dict['model']
            purchase_info.address = post_dict['address'] 
            purchase_info.contact_person = post_dict['contact_person']
            purchase_info.contact_number = post_dict['contact_no']
            purchase_info.installation_requested_date = post_dict['installation_requested_date']
            purchase_info.extra_man_power_request = post_dict['extra_man_power']
            purchase_info.remarks = post_dict['remarks']
            purchase_info.save()
            quantity_delivery_date = QuantityDeliveryDate.objects.create(quantity= post_dict['quantity'], delivery_date=post_dict['delivery_requested_date'])
            purchase_info.delivery_requested_date.add(quantity_delivery_date) 
            purchase_info.save()
            response = simplejson.dumps({'result': 'success', 'message': 'Successfully added'})
        except Exception as ex:
            response = simplejson.dumps({'result': 'error', 'message': str(ex)})
            status_code = 500
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class FetchBrandNames(View):
    def get(self, request, *args, **kwargs):
        ctx_brands = []
        brands =  PurchaseInformation.objects.all().values_list('brand', flat = True).distinct()
        for brand in brands:
            ctx_brands.append({
               'brand_name': brand
            })
        response = simplejson.dumps({'result': 'sucess', 'brands': ctx_brands})
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype = 'application/json')

class PurchaseInfoView(View):

    def get(self, request, *args, **kwargs):

        purchase_info = PurchaseInformation.objects.get(id=kwargs['purchase_info_id'])
        context = {
            'purchase': purchase_info,
        }
        return render(request, 'view_purchase_info.html', context)
    def post(self, request, *args, **kwargs):
        post_dict = request.POST
        purchase_info = PurchaseInformation.objects.get(id=kwargs['purchase_info_id'])
        try:

            quantity = ''
            delivery_date = ''
            for purchase_detail in purchase_info.delivery_requested_date.all():
                quantity = purchase_detail.quantity
                delivery_date = purchase_detail.delivery_date
            if delivery_date != post_dict['delivery_requested_date']:
                quantity_delivery_date = QuantityDeliveryDate.objects.create(quantity= quantity, delivery_date=post_dict['delivery_requested_date'])
                purchase_info.delivery_requested_express_delivery = 'Changed the delivery requested date for quantities : ',quantity,', from date : ',\
                 delivery_date, ', to date : ', post_dict['delivery_requested_date']
                purchase_info.delivery_requested_date.clear()
                purchase_info.delivery_requested_date_change = purchase_info.delivery_requested_date_change + 1
                purchase_info.delivery_requested_date.add(quantity_delivery_date) 
                purchase_info.save()
            if purchase_info.installation_requested_date != post_dict['installation_requested_date']:
                purchase_info.installation_requested_express_delivery = 'Changed the Installation request date from date : ',\
                 purchase_info.installation_requested_date, ', to date : ', post_dict['installation_requested_date']
                purchase_info.installation_requested_date = post_dict['installation_requested_date']
                purchase_info.save()            
            context = {'result': 'success', 'message': 'Successfully Edited','purchase': purchase_info,}
        except Exception as ex:
            print "except == ", str(ex)
            context = {'result': 'error', 'message': str(ex), 'purchase': purchase_info,}
        return render(request,'view_purchase_info.html', context)



        







