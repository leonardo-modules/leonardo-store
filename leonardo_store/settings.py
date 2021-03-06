# -*- coding: utf-8 -*-

from oscar.defaults import *
import os

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_IMAGE_FOLDER = 'eshop'
OSCAR_PROMOTION_FOLDER = 'promotions'
OSCAR_DELETE_IMAGE_FILES = True

# search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# insecure
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

OSCAR_DEFAULT_CURRENCY = 'EUR'

OSCAR_CURRENCY_FORMAT = "#,##0.00 ¤"


def lazy_profile_redirect():
    '''lazy redirect'''
    from leonardo.module.web.widget.application.reverse import app_reverse_lazy
    return app_reverse_lazy(
        'profile-view', 'leonardo_store.apps.customer')

OSCAR_ACCOUNTS_REDIRECT_URL = lazy_profile_redirect()


def lazy_home_redirect():
    '''lazy redirect'''
    from leonardo.module.web.widget.application.reverse import app_reverse_lazy
    return app_reverse_lazy(
        'index', 'leonardo_store.apps.catalogue')

OSCAR_HOMEPAGE = lazy_home_redirect()


def dashboard_access_fn(user, url_name, url_args=None, url_kwargs=None):
    '''No permissions is required

    i recommend use permissions on application if is_stuff and next if is
    need it then make some magic here
    '''
    return user.is_staff

OSCAR_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'leonardo_store.settings.dashboard_access_fn'

'''
This block includes a single pixel from one of the django-oscar
organisation's servers. It's included to keep track of which sites are
running Oscar in production, and what versions of Python and Django are
used. This provides useful data when deciding which versions of Python
and Django to support.

You are, of course, welcome to remove this tracker. To do so, set
OSCAR_TRACKING=False in your settings.
'''
OSCAR_TRACKING = False
