
from django.conf.urls import include, patterns, url


from oscar.apps.catalogue.app import application
from oscar.apps.catalogue.reviews.app import application as reviews_app


urlpatterns = patterns('',
                       (r'^', include(application.get_urls())),
                       (r'^', include(reviews_app.get_urls()))
                       )
