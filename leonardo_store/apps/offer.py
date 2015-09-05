
from django.conf.urls import include, patterns


from oscar.apps.offer.app import application


urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
