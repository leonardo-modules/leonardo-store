
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin, ModelAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *


class ProductItemInlineAdmin(admin.TabularInline):

    model = ProductListItem

    extra = 1


class ProductListAdmin(ModelAdmin):

    inlines = [ProductItemInlineAdmin, ]

admin.site.register(ProductList, ProductListAdmin)
