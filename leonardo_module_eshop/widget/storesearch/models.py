# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from webcms.models import Widget

class StoreSearchWidget(Widget):
    inline = models.BooleanField(verbose_name=_("inline"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("store search")
        verbose_name_plural = _("store searches")
