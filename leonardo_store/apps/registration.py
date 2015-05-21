"""
URLConf for user registration.

"""
from django.conf.urls.defaults import patterns
from livesettings import config_value

urlpatterns = patterns('webcms.module.store.views.registration',
    (r'^$', 'register_contact', {}, 'webcms_store_register_contact'),
)

urlpatterns += patterns('satchmo_store.accounts.views',
    (r'^simple/$', 'register', {}, 'webcms_store_register'),
    (r'^activate/(?P<activation_key>\w+)/$', 'activate', {}, 'webcms_store_registration_activate'),
)

urlpatterns += patterns('django.views.generic',
    (r'^complete/$', 'simple.direct_to_template', {
        'template': 'registration/registration_complete.html',
        'extra_context': {'verify': (config_value('SHOP', 'ACCOUNT_VERIFICATION') == 'EMAIL') }
    }, 'webcms_store_registration_complete'),
)
