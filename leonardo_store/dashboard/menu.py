# transform oscar nav
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from leonardo_admin_dashboard import modules


SKIP_ITEMS = ['page-list', 'content-blocks', ]


def is_enabled(item):
    for i in SKIP_ITEMS:
        if i not in item['url_name']:
            return True
    return False


def get_oscar_dashboard_nav(items, childrens=[]):
    for item in items:
        if 'url_name' in item and is_enabled(item):
            try:
                children = {
                    'title': item['label'],
                    'url': reverse(item['url_name']),
                    'external': False,
                    'icon': item.get('icon', None),
                }
            except:
                pass
            else:
                childrens.append(children)
        if 'children' in item:
            get_oscar_dashboard_nav(item['children'], childrens)


def get_oscar_nav():
    '''Just make this process lazy'''
    childrens = []
    get_oscar_dashboard_nav(settings.OSCAR_DASHBOARD_NAVIGATION, childrens)
    return childrens

# append another link list module for "support".
store_menu = modules.SubMenuLinkList(
    _('Store'),
    children=get_oscar_nav(),
    column=2,
    order=1
)

customers = modules.MenuModelList(
    _('Customers'),
    models=('auth.user', 'customer.*', 'address.*', 'whishlists.*'),
    column=2,
    order=1
)

analytics = modules.MenuModelList(
    _('Analytics'),
    models=('analytics.*', ),
    column=2,
    order=1
)
