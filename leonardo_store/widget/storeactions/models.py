
from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


class StoreActionsWidget(Widget):

    """Simple widget for showing Store Actions in one pack
    """

    inline = models.BooleanField(verbose_name=_("inline"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("quick store actions")
        verbose_name_plural = _("quick store actions")
