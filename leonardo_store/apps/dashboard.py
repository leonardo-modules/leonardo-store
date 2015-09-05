
from django.conf.urls import include, patterns, url


from oscar.apps.dashboard.app import application


urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
