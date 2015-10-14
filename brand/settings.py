
from oscar.defaults import OSCAR_DASHBOARD_NAVIGATION
from django.utils.translation import ugettext_lazy as _

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Trademarks'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Trademarks'),
                'url_name': 'dashboard:brand-list',
            },
            {
                'label': _('Brands'),
                'url_name': 'dashboard:brand-list',
            },
        ]
    })
