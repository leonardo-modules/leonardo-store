
from django.conf.urls import include, patterns, url


from oscar.apps.catalogue.app import application

urlpatterns = patterns('',
    (r'^', include(application.get_urls(), namespace='catalog'),),
)
