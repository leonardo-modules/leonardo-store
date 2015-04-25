
from django.conf.urls import include, patterns, url
from oscar.app import application as oscar_app
from oscarapi.app import application as api


# private eshop urls
urlpatterns = patterns('',
                       url(r'', include(oscar_app.urls)),
                       url(r'api/', include(api.urls)),
                       )
