from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^setup/$', 'webcms.module.store.views.category.category_setup', {}, 'webcms_store_category_setup'),
    (r'^(?P<parent_slugs>([-\w]+/)*)?(?P<slug>[-\w]+)/$', 'product.views.category_view', {}, 'webcms_store_category'),
    (r'^$', 'product.views.category_index', {}, 'webcms_store_category_index'),
)
