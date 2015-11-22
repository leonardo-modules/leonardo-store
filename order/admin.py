
from django.contrib import admin
from oscar.core.loading import get_model

BillingAddress = get_model('order', 'BillingAddress')

try:
    admin.site.register(BillingAddress)
except Exception as e:
    pass
