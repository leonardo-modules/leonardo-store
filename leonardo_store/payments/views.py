import logging

from django import http
from django.contrib import messages
from django.contrib.auth import login
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from oscar.apps.checkout.views import PaymentDetailsView, PaymentMethodView
from oscar.core.loading import get_class

from .repository import Repository

CheckoutSessionData = get_class(
    'checkout.utils', 'CheckoutSessionData')


class LeonardoPaymentMethodView(PaymentMethodView):

    """
    Plugable payments for Oscar/Leonardo Store
    """

    template_name = 'checkout/payment_methods.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LeonardoPaymentMethodView, self).get_context_data(*args, **kwargs)
        context['methods'] = self.get_available_payment_methods()
        return context

    def get(self, request, *args, **kwargs):
        # By default we redirect straight onto the payment details view. Shops
        # that require a choice of payment method may want to override this
        # method to implement their specific logic.
        return TemplateResponse(
            request,
            self.template_name,
            context=self.get_context_data(*args, **kwargs))

    def get_available_payment_methods(self):
        """
        Returns all applicable shipping method objects for a given basket.
        """
        # Shipping methods can depend on the user, the contents of the basket
        # and the shipping address (so we pass all these things to the
        # repository).  I haven't come across a scenario that doesn't fit this
        # system.
        return Repository().methods

    def is_valid_payment_method(self, method_code):
        for method in self.get_available_payment_methods():
            if method.code == method_code:
                return True
        return False

    def get_success_response(self):
        return redirect('checkout:payment-details')

    def post(self, request, *args, **kwargs):

        # Need to check that this code is valid for this user
        method_code = request.POST.get('method_code',
                                       self.checkout_session.payment_method())
        if not self.is_valid_payment_method(method_code):
            messages.error(request, _("Your submitted payment method is not"
                                      " permitted"))
            return redirect('checkout:payment-method')

        # Save the code for the chosen shipping method in the session
        # and continue to the next step.
        self.checkout_session.pay_by(method_code)

        # determine selected payment method
        method = Repository().get_method(method_code)

        # check selection and redirect as GET to payment method
        if request.POST.get('method_code', None):
            request.method = 'GET'

        return method.view.as_view()(request, **kwargs)


class CustomPaymentDetailsView(PaymentDetailsView):

    def get_payment_method(self):
        method_code = self.checkout_session.payment_method()
        return Repository().get_method(method_code)

    def post(self, request, *args, **kwargs):
        payment_method = self.get_payment_method()
        payment_method.view.preview = True
        return payment_method.view.as_view()(request, **kwargs)

    def get(self, request, *args, **kwargs):
        '''get used payment method from session and redirect

        to correct payment detail view

        '''

        if self.checkout_session._get('payment', 'in_detail'):

            payment_method = self.get_payment_method()
            self.checkout_session._set('payment', 'in_detail', True)

            return payment_method.view.as_view()(request, **kwargs)

        return LeonardoPaymentMethodView.as_view()(request, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomPaymentDetailsView, self).get_context_data(
            *args, **kwargs)
        context['payment_method'] = self.get_payment_method()
        return context
