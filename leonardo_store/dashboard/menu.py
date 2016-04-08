
import logging
from django.conf import settings
from leonardo.module.web.widget.application.reverse import app_reverse
from django.utils.translation import ugettext_lazy as _
from leonardo_admin_dashboard import modules

SKIP_ITEMS = ['page-list', 'content-blocks', ]

LOG = logging.getLogger(__name__)


def is_enabled(item):
    for i in SKIP_ITEMS:
        if i not in item['url_name']:
            return True
    return False


def get_oscar_dashboard_nav(items, childrens=[]):
    for item in items:
        if 'url_name' in item and is_enabled(item):
            children = {
                'title': item['label'],
                'external': False,
                'icon': item.get('icon', None),
            }
            try:
                children['url'] = app_reverse(item['url_name'])
            except:
                try:
                    children['url'] = app_reverse(
                        item['url_name'],
                        'leonardo_store.apps.dashboard')
                except Exception as e:
                    # If there are not any app bind to url
                    # this not work
                    if 'children' in item:
                        get_oscar_dashboard_nav(item['children'], childrens)
                    LOG.exception(e)
                    continue
            childrens.append(children)
        if 'children' in item:
            get_oscar_dashboard_nav(item['children'], childrens)


def get_oscar_nav():
    '''Just make this process lazy'''
    childrens = []
    try:
        get_oscar_dashboard_nav(settings.OSCAR_DASHBOARD_NAVIGATION, childrens)
    except:
        # this method fails if there are not any linked apps
        # obviously when you create site etc.
        pass
    return childrens


class StoreSubMenuLinkList(modules.SubMenuLinkList):
    # append another link list module for "support".
    title = _('Store')

    def render(self, request=None):

        if not hasattr(self, 'oscar_nav_loaded'):
            self.children += get_oscar_nav()
            self.oscar_nav_loaded = True

        return super(StoreSubMenuLinkList, self).render(request=request)

    column = 2
    order = 1

store_menu = StoreSubMenuLinkList()

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
