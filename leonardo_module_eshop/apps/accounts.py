from django.conf.urls.defaults import *

from satchmo_store.accounts.urls import urlpatterns as extra_patterns

urlpatterns = patterns('',
    url(r'^$', 'satchmo_store.contact.views.view', name='webcms_store_account_dashboard'),
    url(r'^update/$', 'satchmo_store.contact.views.update', name='webcms_store_account_update'), 
    url(r'^history/$', 'satchmo_store.shop.views.orders.order_history', name='webcms_store_order_list'),
    url(r'^tracking/(?P<order_id>\d+)/$', 'satchmo_store.shop.views.orders.order_tracking', {}, 'webcms_store_order_detail'),
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='webcms_store_password_change'),
    url(r'^password-change-done/$', 'django.contrib.auth.views.password_change_done', name='webcms_store_password_change_done'),
    (r'^contact/$', 'satchmo_store.shop.views.contact.form', {}, 'webcms_store_contact'),
)
