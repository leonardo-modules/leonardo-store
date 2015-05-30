
from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


class StoreContactWidget(Widget):

    """Simple Store Contact for advance features please use Leonardo Stores
    """

    name = models.CharField(max_length=255, verbose_name=_("store name"))
    description = models.TextField(verbose_name=_("store description"))
    email = models.EmailField(verbose_name=_("store email"))
    phone = models.CharField(max_length=255, verbose_name=_("store phone"))
    address = models.TextField(verbose_name=_("store address"))

    class Meta:
        abstract = True
        verbose_name = _("store contact")
        verbose_name_plural = _("store contacts")
