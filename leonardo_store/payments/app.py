
from .repository import Repository

from oscar.apps.checkout.views import PaymentDetailsView
from .views import LeonardoPaymentMethodView


class CustomPaymentDetailsView(PaymentDetailsView):

    def get(self, request, *args, **kwargs):
        '''get used payment method from session and redirect

        to correct payment detail view

        '''

        method_code = self.checkout_session.payment_method()

        if method_code and self.checkout_session._get('payment', 'in_detail'):

            paymet_method = Repository().get_method(method_code)

            return paymet_method.view.as_view()(request, **kwargs)

        self.checkout_session._set('payment', 'in_detail', True)

        return LeonardoPaymentMethodView.as_view()(request, **kwargs)
