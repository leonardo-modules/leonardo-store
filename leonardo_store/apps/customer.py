
from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from oscar.apps.customer.app import application
from oscar.apps.customer import views
from leonardo.module.web.widget.application.reverse import app_reverse_lazy
from oscar.app import application as oscar_app
from oscar.views.decorators import login_forbidden
from django.contrib.auth.tokens import default_token_generator
from oscar.apps.customer import utils, forms
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

views.ProfileUpdateView.success_url = app_reverse_lazy(
    'profile-view', 'leonardo_store.apps.customer')


def get_password_reset_url(user, token_generator=default_token_generator):
    """
    Generate a password-reset URL for a given user
    """
    kwargs = {
        'token': token_generator.make_token(user),
        'uidb64': urlsafe_base64_encode(force_bytes(user.id)),
    }
    return app_reverse_lazy('password-reset-confirm',
                            'leonardo_store.apps.customer', kwargs=kwargs)

utils.get_password_reset_url = get_password_reset_url
forms.get_password_reset_url = get_password_reset_url

urlpatterns = patterns('',
                       url(r'^$',
                           login_required(
                               application.profile_view.as_view()),
                           name='profile-view'),
                       (r'^', include(application.get_urls(),),),

                       )

urlpatterns += [
    # Password reset - as we're using Django's default view functions,
    # we can't namespace these urls as that prevents
    # the reverse function from working.
    url(r'^orders/(?P<order_number>[\w-]*)/(?P<line_id>\d+)/$',
        login_required(application.order_line_view.as_view()),
        name='order-line'),
    url(r'^password-reset/$',
        login_forbidden(auth_views.password_reset),
        {'password_reset_form': oscar_app.password_reset_form,
         'post_reset_redirect': app_reverse_lazy('password-reset-done', 'leonardo_store.apps.customer')},
        name='password-reset'),
    url(r'^password-reset/done/$',
        login_forbidden(auth_views.password_reset_done),
        name='password-reset-done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        login_forbidden(auth_views.password_reset_confirm),
        {
            'post_reset_redirect': app_reverse_lazy('password-reset-complete', 'leonardo_store.apps.customer'),
            'set_password_form': oscar_app.set_password_form,
        },
        name='password-reset-confirm'),
    url(r'^password-reset/complete/$',
        login_forbidden(auth_views.password_reset_complete),
        name='password-reset-complete'),
    url(r'', include(oscar_app.promotions_app.urls)),
]
