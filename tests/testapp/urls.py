from __future__ import absolute_import, unicode_literals


from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'', include('leonardo.urls')),
    url(r'', include('leonardo_store.apps.checkout', namespace='checkout')),
    url(r'', include('leonardo_store.apps.customer', namespace='customer')),
    url(r'', include('leonardo_store.apps.catalogue', namespace='catalogue')),
)
