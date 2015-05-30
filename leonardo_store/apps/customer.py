
from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from oscar.apps.customer.app import application
from oscar.apps.customer import views
from leonardo.module.web.widget.application.reverse import app_reverse_lazy


views.ProfileUpdateView.success_url = app_reverse_lazy(
        'profile-view', 'leonardo_store.apps.customer')

urlpatterns = patterns('',
                       url(r'^$',
                           login_required(
                               application.profile_view.as_view()),
                           name='profile-view'),
                       (r'^', include(application.get_urls(),),),

                       )
