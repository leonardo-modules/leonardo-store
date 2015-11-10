
from django.contrib import admin
from oscar.core.loading import get_model

BillingAddress = get_model('order', 'BillingAddress')

admin.site.register(BillingAddress)
