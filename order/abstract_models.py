from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import (AbstractBillingAddress,
                                                AbstractShippingAddress,
                                                PhoneNumberField)


class AbstractAddressExtension(models.Model):

    '''This is common address extension'''

    company_name = models.CharField(
        max_length=255, verbose_name=_("company name"), blank=True, null=True)
    company_id = models.CharField(
        max_length=255, verbose_name=_("company ID"), blank=True, null=True)
    vat_id = models.CharField(
        max_length=255, verbose_name=_("VAT ID"), blank=True, null=True)
    bank_account = models.CharField(
        max_length=255, verbose_name=_("bank account"), blank=True, null=True)
    bank_code = models.CharField(
        max_length=255, verbose_name=_("bank code"), blank=True, null=True)

    class Meta:
        abstract = True


class AbstractShippingAddress(AbstractShippingAddress, AbstractAddressExtension):

    @property
    def salutation(self):
        """
        Name (including title)
        """
        if self.company_name and self.company_id and self.vat_id:
            return self.join_fields(
                ('company_name', 'company_id', 'vat_id'),
                separator=u" ")
        return self.join_fields(
            ('title', 'first_name', 'last_name'),
            separator=u" ")

    class Meta:
        abstract = True
        # ShippingAddress is registered in order/models.py
        app_label = 'order'
        verbose_name = _("Shipping address")
        verbose_name_plural = _("Shipping addresses")


class AbstractBillingAddress(AbstractBillingAddress, AbstractAddressExtension):

    @property
    def salutation(self):
        """
        Name (including title)
        """
        if self.company_name and self.company_id and self.vat_id:
            return self.join_fields(
                ('company_name', 'company_id', 'vat_id'),
                separator=u" ")
        return self.join_fields(
            ('title', 'first_name', 'last_name'),
            separator=u" ")

    class Meta:
        abstract = True
        # BillingAddress is registered in order/models.py
        app_label = 'order'
        verbose_name = _("Billing address")
        verbose_name_plural = _("Billing addresses")

    phone_number = PhoneNumberField(
        _("Phone number"), blank=True,
        help_text=_("In case we need to call you about your order"))
    notes = models.TextField(
        blank=True, verbose_name=_('Instructions'),
        help_text=_("Tell us anything we should know when delivering "
                    "your order."))
