
from django.conf.urls import include, patterns
from django.shortcuts import redirect
from feincms.views.decorators import standalone
from leonardo.module.web.widget.application.reverse import (app_reverse,
                                                            app_reverse_lazy)
from oscar.apps.checkout import mixins, views
from oscar.apps.checkout.app import application
from oscar.core.loading import get_model

views.ShippingAddressView.get = standalone(views.ShippingAddressView.get)
views.PaymentDetailsView.get = standalone(views.PaymentDetailsView.get)
views.ThankYouView.get = standalone(views.ThankYouView.get)


def shipping_address(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return redirect(app_reverse(
        'shipping-address', 'leonardo_store.apps.checkout'))

views.IndexView.get_success_response = shipping_address


def shipping_method(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return redirect(app_reverse('shipping-method', 'leonardo_store.apps.checkout'))

views.ShippingAddressView.get_success_response = shipping_method
views.ShippingAddressView.get_success_url = lambda o: app_reverse_lazy(
    'shipping-method', 'leonardo_store.apps.checkout')


def get_success_response(self):
    return redirect(app_reverse_lazy(
        'payment-method', 'leonardo_store.apps.checkout'))


def payment_detail(self):
    return redirect(app_reverse_lazy(
        'payment-details', 'leonardo_store.apps.checkout'))

# patched get_initial


Country = get_model('address', 'Country')


def get_initial(self):
    initial = self.checkout_session.new_shipping_address_fields()
    if initial:
        #if 'country' not in initial or not isinstance(initial['country'], Country):
        # Convert the primary key stored in the session into a Country
        # instance
        try:
            initial['country'] = Country.objects.get(
                iso_3166_1_a2=initial.pop('country_id'))
        except Country.DoesNotExist:
            # Hmm, the previously selected Country no longer exists. We
            # ignore this.
            pass
        except KeyError:
            pass
    return initial

views.ShippingAddressView.get_initial = get_initial

mixins.OrderPlacementMixin.success_url = app_reverse_lazy(
    'thank-you', 'leonardo_store.apps.checkout')


views.ShippingMethodView.get_success_response = get_success_response
views.PaymentMethodView.get_success_response = payment_detail

urlpatterns = patterns('',
                       (r'^', include(application.get_urls()),),
                       )
