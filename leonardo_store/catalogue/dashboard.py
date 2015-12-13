from django import forms
from django.core import exceptions
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from treebeard.forms import movenodeform_factory

from oscar.core.loading import get_class, get_model
from oscar.core.utils import slugify
from oscar.forms.widgets import ImageInput

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
Category = get_model('catalogue', 'Category')
StockRecord = get_model('partner', 'StockRecord')
ProductCategory = get_model('catalogue', 'ProductCategory')
ProductImage = get_model('catalogue', 'ProductImage')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')
ProductSelect = get_class('dashboard.catalogue.widgets', 'ProductSelect')

from oscar.apps.dashboard.catalogue.forms import ProductAttributesForm


class ProductAttributesForm(ProductAttributesForm):

    class Meta:
        model = ProductAttribute
        fields = ["name", "code", "type",
                  "default_value",
                  "option_group", "required",
                  "is_hidden", "help_text"]

ProductAttributesFormSet = inlineformset_factory(ProductClass,
                                                 ProductAttribute,
                                                 form=ProductAttributesForm,
                                                 extra=3)


def patch_product_class_attributes():

    from oscar.apps.dashboard.catalogue.views import ProductClassCreateUpdateView
    ProductClassCreateUpdateView.product_attributes_formset = ProductAttributesFormSet
