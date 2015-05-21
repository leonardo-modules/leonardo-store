
from django.conf.urls import include, patterns, url


from oscar.app import application

urlpatterns = patterns('',
    (r'^', include(application.get_urls(), namespace='eshop'),),
)
