
def override_checkout():
    '''just override checkout ``payment_method_view``'''
    from oscar.apps.checkout.app import application
    from leonardo_store.payments.views import LeonardoPaymentMethodView
    application.payment_method_view = LeonardoPaymentMethodView
    from leonardo_store.payments.app import CustomPaymentDetailsView
    application.payment_details_view = CustomPaymentDetailsView
