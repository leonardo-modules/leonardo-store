"""
URLConf for Django user authentication.
"""
from django.conf.urls.defaults import patterns

urlpatterns = patterns('satchmo_store.accounts.views',
    (r'^$', 'emaillogin', { 'template_name': 'registration/login.html' }, 'webcms_store_login'),
    (r'^secure/$', 'emaillogin', { 'SSL' : True, 'template_name': 'registration/login.html' }, 'webcms_store_secure_login'),
)

urlpatterns += patterns('django.contrib.auth.views',
    ('^logout/$','logout', {'template_name': 'registration/logout.html'}, 'webcms_store_logout'),
)

urlpatterns += patterns('webcms.module.store.views.auth',
    (r'^reset/$', 'password_reset', {}, 'webcms_store_password_reset'),
    (r'^reset/sent/$', 'password_reset_done', {'template_name':'registration/password_reset_done.html'}, 'webcms_store_password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {}, 'webcms_store_password_reset_confirm'),
    (r'^reset/complete/$', 'password_reset_complete', {}, 'webcms_store_password_reset_complete'),
)
