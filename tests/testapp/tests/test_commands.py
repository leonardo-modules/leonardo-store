from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.six.moves import http_client
from oscar.core.loading import get_class, get_model
from oscar.test.testcases import WebTestCase
from django.core import management
from leonardo.models import Page

from ._utils import CheckoutMixin

Order = get_model('order', 'Order')
ConditionalOffer = get_model('offer', 'ConditionalOffer')
UserAddress = get_model('address', 'UserAddress')
GatewayForm = get_class('checkout.forms', 'GatewayForm')


class LeonardoWebTestCase(WebTestCase):

    @property
    def page(self):
        return Page.objects.first()

    def setUp(self):
        super(LeonardoWebTestCase, self).setUp()

        management.call_command('gitrestore',
                                url="git@repo1.robotice.cz:majklk/store-backup.git")


class TestThankYouView(CheckoutMixin, LeonardoWebTestCase):

    def tests_gets_a_404_when_there_is_no_order(self):
        response = self.get(
            reverse('checkout:thank-you'), user=self.user, status="*")
        self.assertEqual(http_client.NOT_FOUND, response.status_code)

    def tests_custumers_can_reach_the_thank_you_page(self):
        self.add_product_to_basket()
        self.enter_shipping_address()
        thank_you = self.place_order()
        self.assertIsOk(thank_you)

    def test_superusers_can_force_an_order(self):
        self.add_product_to_basket()
        self.enter_shipping_address()
        self.place_order()
        user = self.create_user('admin', 'admin@admin.com')
        user.is_superuser = True
        user.save()
        order = Order.objects.get()

        test_url = '%s?order_number=%s' % (
            reverse('checkout:thank-you'), order.number)
        response = self.get(test_url, status='*', user=user)
        self.assertIsOk(response)

        test_url = '%s?order_id=%s' % (reverse('checkout:thank-you'), order.pk)
        response = self.get(test_url, status='*', user=user)
        self.assertIsOk(response)

    def test_users_cannot_force_an_other_custumer_order(self):
        self.add_product_to_basket()
        self.enter_shipping_address()
        self.place_order()
        user = self.create_user('John', 'john@test.com')
        user.save()
        order = Order.objects.get()

        test_url = '%s?order_number=%s' % (
            reverse('checkout:thank-you'), order.number)
        response = self.get(test_url, status='*', user=user)
        self.assertEqual(response.status_code, http_client.NOT_FOUND)

        test_url = '%s?order_id=%s' % (reverse('checkout:thank-you'), order.pk)
        response = self.get(test_url, status='*', user=user)
        self.assertEqual(response.status_code, http_client.NOT_FOUND)
