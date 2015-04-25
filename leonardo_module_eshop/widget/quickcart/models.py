# -#- coding: utf-8 -#-

from django import forms

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from webcms.models import Widget

class QuickCartWidget(Widget):
    show_items = models.BooleanField(verbose_name=_("show items"), default=True)
    inline = models.BooleanField(verbose_name=_("inline"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("quick cart")
        verbose_name_plural = _("quick carts")
