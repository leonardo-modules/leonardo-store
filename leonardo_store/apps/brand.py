from django.conf.urls.defaults import *

urlpatterns = patterns('satchmo_ext.brand.views',
    (r'^$', 'brand_list', {}, 'webcms_store_brand_list'),
    (r'^(?P<brandname>.*)/(?P<catname>.*)/$', 'brand_category_page', {}, 'webcms_store_brand_category'),
    (r'^(?P<brandname>.*)/$', 'brand_page', {}, 'webcms_store_brand'),
)
