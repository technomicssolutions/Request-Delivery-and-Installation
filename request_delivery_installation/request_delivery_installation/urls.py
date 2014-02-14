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
    url(r'^register/$', Signup.as_view(), name='register'),
    url(r'^dealer/(?P<user_id>[\d+]+)/add/subdealer/$',login_required(AddSubDealer.as_view()), name="add_subdealer"),
    url(r'^add_purchase_info/$', AddPurchanseInfo.as_view(), name='add_purchase_info'),
    url(r'^fetch_brand_names/$', FetchBrandNames.as_view(), name='fetch_brand_names'),
    # url(r'^logout/$', Logout.as_view(), name='logout_web'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
