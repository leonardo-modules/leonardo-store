from django.utils import six
from import_export import fields
from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')
Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')
Product = get_model('catalogue', 'Product')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')


class CategoryField(fields.Field):

    '''Support categories as comma delimited list

    creates only root level categories if not exist
    '''

    def export(self, obj):
        return ','.join(self.get_value(obj))

    def get_value(self, obj):
        return [c.category.slug
                for c in obj.productcategory_set.all()]

    def clean(self, data):
        """
        Takes value stored in the data for the field and returns it as
        appropriate python object.
        """
        value = data.get('categories', '')

        if value != '':
            categories = []
            for category_slug in value.split(','):
                category, created = Category.objects.get_or_create(
                    slug=category_slug,
                    defaults={'depth': 1})
                categories.append(category)

            return categories
        return []

    def save(self, obj, data):
        """
        Cleans this field value and assign it to provided object.
        """
        categories = self.clean(data)

        for category in categories:
            product_category, created = ProductCategory.objects.update_or_create(
                product=obj, category=category,
                defaults={'product': obj,
                          'category': category})


STOCK_RECORD_FIELDS = ('id', 'product', 'product__title', 'partner',
                       'partner__name', 'product__categories',
                       'partner_sku', 'price_currency', 'price_excl_tax',
                       'price_retail',  'cost_price', 'num_in_stock',
                       'num_allocated', 'low_stock_threshold')


class ProductMixin(object):

    def get_product(self, data):
        return Product.objects.get(
            upc=data.get('upc'))


class StockRecordsField(fields.Field, ProductMixin):

    '''load and save StockRecord fields on product

    if partner_sku is null create and uses Default Partner
    '''

    def get_partner(self, data):
        partner_name = data.get('partner', '')

        if partner_name != '':
            partner = Partner.objects.get(
                name=partner_name)
            return partner
        return None

    def save(self, obj, data):
        """
        Cleans this field value and assign it to provided object.
        """

        value = self.clean(data)

        partner = self.get_partner(data)

        if not partner or not value or self.attribute in ['partner']:
            return

        product = self.get_product(data)

        stock_record, created = StockRecord.objects.update_or_create(
            product=product, partner=partner,
            defaults={
                self.attribute: value
            })

    def get_value(self, obj):
        """
        Returns value for this field from object attribute.
        """

        if obj.stockrecords.exists():
            return getattr(obj.stockrecords.first(), self.attribute)
        return None


class AttributeField(fields.Field, ProductMixin):

    '''load and save ProductAttributes

    '''

    def get_attribute(self, data):
        return self.get_product(data).get_product_class().attributes.get(code=self.attribute)

    def save(self, obj, data):
        """
        Cleans this field value and assign it to provided object.
        """

        value = self.clean(data)

        try:
            attr = self.get_attribute(data)
        except ProductAttribute.DoesNotExist:
            pass
        else:
            # check type

            if isinstance(value, six.text_type):
                defaults = {
                    'value_text': value
                }

            elif isinstance(value, six.integer_types):
                defaults = {
                    'value_integer': value
                }
            else:
                defaults = {
                    'value_float': value
                }

            product_attribute, created = ProductAttributeValue.objects.update_or_create(
                attribute=attr, product=self.get_product(data),
                defaults=defaults)

    def get_value(self, obj):
        """
        Returns value for this field from object attribute.
        """

        try:
            attr = obj.get_product_class().attributes.get(code=self.attribute)
        except ProductAttribute.DoesNotExist:
            pass
        else:
            return obj.attribute_values.get(attribute=attr)
        return None
