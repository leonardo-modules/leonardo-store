# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string

from satchmo_store.shop.models import Config

from feincms.content.application.models import reverse
from webcms.models import Widget
from webcms.utils.models import MultiSelectField

CONTACT_CHOICES = (
    ('name', _('Store name')),
    ('description', _('Store description')),
    ('e-mail', _('Store e-mail')),
    ('phone', _('Phone number')),
    ('address', _('Address')),
)

class StoreContactWidget(Widget):
    show_details = MultiSelectField(max_length=255, verbose_name=_("show details"), choices=CONTACT_CHOICES)

    class Meta:
        abstract = True
        verbose_name = _("store contact")
        verbose_name_plural = _("store contacts")

    def render_content(self, options):
        request = options.pop('request')

        shop = Config.objects.get_current()

        context = RequestContext(request, {
            'widget': self,
            'shop': shop,
        })

        return render_to_string(self.template_name, context)
