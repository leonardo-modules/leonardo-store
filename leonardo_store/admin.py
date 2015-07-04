
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin, ModelAdmin
from django.utils.translation import ugettext_lazy as _
from leonardo_import_export.admin import ImportExportModelAdmin
from oscar.apps.catalogue.admin import ProductAdmin as OscarProductAdmin
from oscar.apps.catalogue.admin import CategoryAdmin as OscarCategoryAdmin
from oscar.core.loading import get_model

from .models import *
from .resources import *

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')
UserAddress = get_model('address', 'UserAddress')
Order = get_model('order', 'Order')
Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')


class ProductAdmin(OscarProductAdmin, ImportExportModelAdmin):
    resource_class = ProductResource

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(ImportExportModelAdmin, OscarCategoryAdmin):
    resource_class = CategoryResource
    list_display = ('name', 'path')

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)


from oscar.apps.address.admin import UserAddressAdmin  # noqa


class UserAddressAdmin(ImportExportModelAdmin):
    resource_class = UserAddressResource

admin.site.unregister(UserAddress)
admin.site.register(UserAddress, UserAddressAdmin)


from oscar.apps.order.admin import OrderAdmin  # noqa


class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource

admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)

from oscar.apps.partner.admin import *


class PartnerAdmin(ImportExportModelAdmin):
    resource_class = PartnerResource

admin.site.unregister(Partner)
admin.site.register(Partner, PartnerAdmin)


class StockRecordAdmin(ImportExportModelAdmin):
    resource_class = StockRecordResource

admin.site.unregister(StockRecord)
admin.site.register(StockRecord, StockRecordAdmin)


class ProductItemInlineAdmin(admin.TabularInline):

    model = ProductListItem

    extra = 1


class ProductListAdmin(ModelAdmin):

    inlines = [ProductItemInlineAdmin, ]

admin.site.register(ProductList, ProductListAdmin)
