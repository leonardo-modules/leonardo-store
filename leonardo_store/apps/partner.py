
from django.conf.urls import include, patterns, url


from oscar.apps.partner.app import application


urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
