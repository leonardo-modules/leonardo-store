from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('satchmo_store.shop.views',
    (r'^$', 'search.search_view', {}, 'webcms_store_search'),
)

