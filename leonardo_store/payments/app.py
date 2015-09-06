
from .repository import Repository

from oscar.apps.checkout.views import PaymentDetailsView
from .views import LeonardoPaymentMethodView


class CustomPaymentDetailsView(PaymentDetailsView):

    def get_payment_method(self):

        method_code = self.checkout_session.payment_method()
        return Repository().get_method(method_code)

    def get(self, request, *args, **kwargs):
        '''get used payment method from session and redirect

        to correct payment detail view

        '''

        if self.checkout_session._get('payment', 'in_detail'):

            payment_method = self.get_payment_method()

            return payment_method.view.as_view()(request, **kwargs)

        self.checkout_session._set('payment', 'in_detail', True)

        return LeonardoPaymentMethodView.as_view()(request, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomPaymentDetailsView, self).get_context_data(
            *args, **kwargs)
        context['payment_method'] = self.get_payment_method()
        return context
