
from django.conf.urls import patterns, url
from django.contrib import admin, messages
from django.contrib.admin.options import InlineModelAdmin, ModelAdmin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from leonardo.module.media.models import Image
from leonardo_import_export.admin import ImportExportModelAdmin
from oscar.apps.address.admin import UserAddressAdmin  # noqa
from oscar.apps.catalogue.admin import CategoryAdmin as OscarCategoryAdmin
from oscar.apps.catalogue.admin import ProductAdmin as OscarProductAdmin
from oscar.apps.order.admin import OrderAdmin  # noqa
from oscar.apps.partner.admin import *
from oscar.core.loading import get_model
from treebeard.forms import movenodeform_factory

from .models import *
from .resources import *

Product = get_model('catalogue', 'Product')
ProductImage = get_model('catalogue', 'ProductImage')
Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')
UserAddress = get_model('address', 'UserAddress')
Order = get_model('order', 'Order')
Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')


class ProductAdmin(OscarProductAdmin, ImportExportModelAdmin):
    resource_class = ProductResource

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)



class ProductImageAdmin(ImportExportModelAdmin):
    resource_class = ProductImageResource
    change_list_template = 'admin/change_list_with_scan.html'

    def get_urls(self):
        urls = super(ProductImageAdmin, self).get_urls()
        info = self.get_model_info()
        my_urls = patterns(
            '',
            url(r'^scan/$',
                self.admin_site.admin_view(self.scan_action),
                name='%s_%s_scan_images' % info),
        )
        return my_urls + urls

    def scan_action(self, request, *args, **kwargs):
        '''
        Perform the product image scan
        '''

        for product in Product.objects.all():
            images = Image.objects.filter(
                Q(name__icontains=product.upc) |
                Q(original_filename__icontains=product.upc))

            for i, image in enumerate(images):
                product_image = ProductImage(
                    product=product)
                product_image.original.save(
                    image.original_filename,
                    image.file, save=False)
                product_image.display_order = i
                try:
                    product_image.save()
                except:
                    product_image.original.save(
                        image.original_filename,
                        image.file, save=False)

        success_message = _('Scan finished')
        messages.success(request, success_message)

        url = reverse('admin:%s_%s_changelist' % self.get_model_info(),
                      current_app=self.admin_site.name)
        return HttpResponseRedirect(url)

admin.site.unregister(ProductImage)
admin.site.register(ProductImage, ProductImageAdmin)


class CategoryAdmin(OscarCategoryAdmin, ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('name', 'path', 'slug')
    form = movenodeform_factory(Category)

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)


class ProductCategoryAdmin(ImportExportModelAdmin):
    resource_class = ProductCategoryResource

admin.site.unregister(ProductCategory)
admin.site.register(ProductCategory, ProductCategoryAdmin)




class UserAddressAdmin(ImportExportModelAdmin):
    resource_class = UserAddressResource

admin.site.unregister(UserAddress)
admin.site.register(UserAddress, UserAddressAdmin)




class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource

admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)



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
