
from django.conf.urls import include, patterns
from oscar.apps.checkout.app import application
from oscar.apps.checkout import views
from oscar.apps.checkout import mixins
from feincms.views.decorators import standalone
from django.shortcuts import redirect
from leonardo.module.web.widget.application.reverse import app_reverse_lazy

views.ShippingAddressView.get = standalone(views.ShippingAddressView.get)
views.PaymentDetailsView.get = standalone(views.PaymentDetailsView.get)


def shipping_address(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return redirect(app_reverse(
        'shipping-address', 'leonardo_store.apps.checkout'))

views.IndexView.get_success_response = shipping_address


def shipping_method(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return redirect(app_reverse('shipping-method', 'leonardo_store.apps.checkout'))

views.ShippingAddressView.get_success_response = shipping_method
views.ShippingAddressView.get_success_url = lambda o: app_reverse_lazy('shipping-method', 'leonardo_store.apps.checkout')


def get_success_response(self):
    return redirect(app_reverse_lazy(
        'payment-method', 'leonardo_store.apps.checkout'))


def payment_detail(self):
    return redirect(app_reverse_lazy(
        'payment-details', 'leonardo_store.apps.checkout'))

mixins.OrderPlacementMixin.get_success_url = app_reverse_lazy(
    'thank-you', 'leonardo_store.apps.checkout')

views.ShippingMethodView.get_success_response = get_success_response
views.PaymentMethodView.get_success_response = payment_detail

urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
