from django.conf.urls.defaults import *

from satchmo_store.accounts.urls import urlpatterns as extra_patterns

urlpatterns = patterns('satchmo_ext.wishlist.views',
     (r'^$', 'wishlist_view', {}, 'webcms_store_wishlist'),
#     (r'^add/$', 'wishlist_add', {}, 'webcms_store_wishlist_add'),
#     (r'^add/ajax/$', 'wishlist_add_ajax', {}, 'webcms_store_wishlist_add_ajax'),
#     (r'^remove/$', 'wishlist_remove', {}, 'webcms_store_wishlist_remove'),
#     (r'^remove/ajax$', 'wishlist_remove_ajax', {}, 'webcms_store_wishlist_remove_ajax'),
     (r'^add_cart/$', 'wishlist_move_to_cart', {}, 'webcms_store_wishlist_move_to_cart'),
)

urlpatterns += patterns('webcms.module.store.views.wishlist',
     (r'^add/(?P<object_id>[0-9]+)/$', 'wishlist_add', {}, 'webcms_store_wishlist_add'),
     (r'^remove/(?P<object_id>[0-9]+)/$', 'wishlist_remove', {}, 'webcms_store_wishlist_remove'),
)
