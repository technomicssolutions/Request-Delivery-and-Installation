from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

from web.views import *

urlpatterns = patterns('',
    
    url(r'^$', login_required(Home.as_view()), name='home'),
    url(r'^accounts/login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^register/$', login_required(Signup.as_view()), name='register'),
    url(r'^dealer/(?P<user_id>[\d+]+)/add/subdealer/$',login_required(AddSubDealer.as_view()), name="add_subdealer"),
    url(r'^add_purchase_info/$', login_required(AddPurchanseInfo.as_view()), name='add_purchase_info'),
    url(r'^fetch_brand_names/$', FetchBrandNames.as_view(), name='fetch_brand_names'),
    url(r'^fetch_purchase_sales_men/$', FetchPurchaseSalesManList.as_view(), name='fetch_purchase_sales_men'),
    url(r'^fetch_dealers/$', FetchDealersList.as_view(), name='fetch_dealers'),
    url(r'^purchase_info/(?P<purchase_info_id>[\d+]+)/$', login_required(PurchaseInfoView.as_view()), name='purchase_info'),
    url(r'^search_purchase_info/(?P<delivery_order_number>[\w-]+)/$', login_required(SearchPurchaseInfo.as_view()), name="search_purchase_info"),
    url(r'^fetch_dealer_company_names/$', FetchFirmNames.as_view(), name='fetch_firm_names'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
