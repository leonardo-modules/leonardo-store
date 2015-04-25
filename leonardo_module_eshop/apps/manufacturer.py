from django.conf.urls.defaults import *

urlpatterns = patterns('webcms.module.store.ext.manufacturer.views',
    (r'^$', 'manufacturer_list', {}, 'webcms_store_manufacturer_list'),
    (r'^(?P<name>.*)/$', 'manufacturer_detail', {}, 'webcms_store_manufacturer_detail'),
)
