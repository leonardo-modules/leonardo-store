
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


class ProfileActionsWidget(Widget):

    class Meta:
        abstract = True
        verbose_name = _("store profile actions")
        verbose_name_plural = _("store profile actions")
