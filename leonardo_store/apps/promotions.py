
from django.conf.urls import include, url

from oscar.apps.promotions.app import application

urlpatterns = [
    url(r'', include(application.urls)),
]
