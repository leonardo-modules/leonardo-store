
def override_address():
    '''just override checkout ``payment_method_view``'''
    from oscar.apps.checkout.app import application
    from oscar.apps.checkout import views
    from .forms import UserAddressForm
    views.UserAddressUpdateView.form_class = UserAddressForm
    application.user_address_update_view = views.UserAddressUpdateView
