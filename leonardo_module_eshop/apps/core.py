from django.conf.urls.defaults import patterns, include
from satchmo_store import shop
from satchmo_store.shop.views.sitemaps import sitemaps

urlpatterns = patterns('satchmo_store.shop.views',
    (r'^$','home.home', {}, 'webcms_store_home'),
    (r'^add/$', 'smart.smart_add', {}, 'webcms_store_smart_add'),
    (r'^contact/$', 'contact.form', {}, 'webcms_store_contact'),
#    (r'^quickorder/$', 'cart.add_multiple', {}, 'webcms_store_quick_order'),
    (r'^search/$', 'search.search_view', {}, 'webcms_store_search'),
)

urlpatterns += patterns('webcms.module.store.views.base',
    (r'^continue-shopping/$', 'continue_shopping', {}, 'webcms_store_continue_shopping'),
)

urlpatterns += patterns('',
    (r'^contact/thankyou/$','django.views.generic.simple.direct_to_template', {'template':'shop/contact_thanks.html'}, 'satchmo_contact_thanks'),
#    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, 'satchmo_sitemap_xml'),
)
