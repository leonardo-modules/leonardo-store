from django.db import models
from oscar.core import compat
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    """
    Simple User profile model
    """
    user = models.OneToOneField(compat.AUTH_USER_MODEL, related_name="profile",
                                blank=True, null=True)
    MALE, FEMALE = 'M', 'F'
    choices = (
        (MALE, 'Male'),
        (FEMALE, 'Female'))
    gender = models.CharField(max_length=1, choices=choices,
                              verbose_name='Gender', blank=True, null=True)
    age = models.PositiveIntegerField(
        verbose_name='Age', blank=True, null=True)

    company_name = models.CharField(
        max_length=255, verbose_name=_("company name"), blank=True, null=True)
    company_id = models.CharField(
        max_length=255, verbose_name=_("company ID"), blank=True, null=True)
    vat_id = models.CharField(
        max_length=255, verbose_name=_("VAT ID"), blank=True, null=True)
    account = models.CharField(
        max_length=255, verbose_name=_("account number"),
        blank=True, null=True)
    bank = models.CharField(
        max_length=255, verbose_name=_("bank"), blank=True, null=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
