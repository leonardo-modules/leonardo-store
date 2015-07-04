
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from feincms.module.page.extensions.navigation import (
    NavigationExtension, PagePretender)


class StoreCategoriesNavigationExtension(NavigationExtension):

    """
    Navigation extension for Leonardo Store
    which lists all available categories
    """

    name = _('Store categories')

    def children(self, page, **kwargs):
        from oscar.core.loading import get_class

        Category = get_class('catalogue.categories', 'Category')
        categories = Category.objects.all()
        for category in categories:
            yield PagePretender(
                title=category.name,
                url=category.get_absolute_url(),
                tree_id=page.tree_id,
                level=page.level + 1,
                language=getattr(page, 'language', settings.LANGUAGE_CODE),
                slug=category.slug,
                parent=page,
                parent_id=page.id,
                lft=page.lft,
                rght=page.rght,
                _mptt_meta=getattr(page, '_mptt_meta', None),
            )
