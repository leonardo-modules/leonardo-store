
from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.template.defaultfilters import slugify
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
from oscar.core.loading import get_model
from oscar.core.validators import non_python_keyword
from oscar.models.fields import AutoSlugField

from . import utils
from .default_field_types import FIELD_TYPES

FORM_DESIGNER_FIELD_TYPES = 'catalogue.default_field_types.FIELD_TYPES'


def get_type_choices():
    return [r[:2] for r in
            utils.get_object(FORM_DESIGNER_FIELD_TYPES)]


class DynamicOptionsMixin(object):

    def clean(self):
        if self.choices and not isinstance(self.get_type(), forms.ChoiceField):
            raise forms.ValidationError(
                _("You can't specify choices for %s fields") % self.type)

    def get_choices(self):
        get_tuple = lambda value: (slugify(value.strip()), value.strip())
        choices = [get_tuple(value) for value in self.choices.split(',')]
        if not self.is_required and self.type == 'select':
            choices = BLANK_CHOICE_DASH + choices
        return tuple(choices)

    def get_type(self, **kwargs):
        types = dict((r[0], r[2])
                     for r in utils.get_object(FORM_DESIGNER_FIELD_TYPES))
        return types[self.type](**kwargs)

    def formfield(self):
        kwargs = dict(
            label=self.name,
            required=self.is_required,
            initial=self.default_value,
        )
        if self.choices:
            kwargs['choices'] = self.get_choices()
        if self.help_text:
            kwargs['help_text'] = self.help_text
        return self.get_type(**kwargs)


class AbstractOption(models.Model, DynamicOptionsMixin):
    """
    Extended version of Oscar AbstractOption

    """
    name = models.CharField(_("Name"), max_length=128)
    code = AutoSlugField(_("Code"), max_length=128, unique=True,
                         populate_from='name')

    choices = models.CharField(
        _('choices'), max_length=1024, blank=True,
        help_text=_('Comma-separated'))

    is_required = models.BooleanField(_('is required'), default=True)

    is_hidden = models.BooleanField(_('is hidden'), default=False)

    type = models.CharField(
        _('type'), max_length=20, choices=lazy(get_type_choices, list)())

    help_text = models.CharField(
        _('help text'), max_length=1024, blank=True,
        help_text=_('Optional extra explanatory text beside the field'))
    default_value = models.CharField(
        _('default value'), max_length=255, blank=True,
        help_text=_('Optional default value of the field'))

    class Meta:
        abstract = True
        app_label = 'catalogue'
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    def __str__(self):
        return self.name


class AbstractProductAttribute(models.Model, DynamicOptionsMixin):
    """
    Defines an attribute for a product class. (For example, number_of_pages for
    a 'book' class)
    """
    product_class = models.ForeignKey(
        'catalogue.ProductClass', related_name='attributes', blank=True,
        null=True, verbose_name=_("Product type"))
    name = models.CharField(_('Name'), max_length=128)
    code = models.SlugField(
        _('Code'), max_length=128,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z_][0-9a-zA-Z_]*$',
                message=_(
                    "Code can only contain the letters a-z, A-Z, digits, "
                    "and underscores, and can't start with a digit.")),
            non_python_keyword
        ])

    # Obsolete Attribute types
    TEXT = "text"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    FLOAT = "float"
    RICHTEXT = "richtext"
    DATE = "date"
    OPTION = "option"
    ENTITY = "entity"
    FILE = "file"
    IMAGE = "image"
    TYPE_CHOICES = (
        (TEXT, _("Text")),
        (INTEGER, _("Integer")),
        (BOOLEAN, _("True / False")),
        (FLOAT, _("Float")),
        (RICHTEXT, _("Rich Text")),
        (DATE, _("Date")),
        (OPTION, _("Option")),
        (ENTITY, _("Entity")),
        (FILE, _("File")),
        (IMAGE, _("Image")),
    )

    type = models.CharField(
        _('type'), max_length=20, choices=lazy(get_type_choices, list)())

    option_group = models.ForeignKey(
        'catalogue.AttributeOptionGroup', blank=True, null=True,
        verbose_name=_("Option Group"),
        help_text=_('Select an option group if using type "Option"'))

    required = models.BooleanField(_('Required'), default=False)
    is_hidden = models.BooleanField(_('is hidden'), default=False)

    help_text = models.CharField(
        _('help text'), max_length=1024, blank=True,
        help_text=_('Optional extra explanatory text beside the field'))

    default_value = models.CharField(
        _('default value'), max_length=255, blank=True,
        help_text=_('Optional default value of the field'))

    class Meta:
        abstract = True
        app_label = 'catalogue'
        ordering = ['code']
        verbose_name = _('Product attribute')
        verbose_name_plural = _('Product attributes')

    @property
    def is_required(self):
        '''just proxy because oscar has hidden'''
        return self.hidden

    @property
    def is_option(self):
        return self.type == self.OPTION

    @property
    def is_file(self):
        return self.type in [self.FILE, self.IMAGE]

    def __str__(self):
        return self.name

    def save_value(self, product, value):
        ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
        try:
            value_obj = product.attribute_values.get(attribute=self)
        except ProductAttributeValue.DoesNotExist:
            # FileField uses False for announcing deletion of the file
            # not creating a new value
            delete_file = self.is_file and value is False
            if value is None or value == '' or delete_file:
                return
            value_obj = ProductAttributeValue.objects.create(
                product=product, attribute=self)

        if self.is_file:
            # File fields in Django are treated differently, see
            # django.db.models.fields.FileField and method save_form_data
            if value is None:
                # No change
                return
            elif value is False:
                # Delete file
                value_obj.delete()
            else:
                # New uploaded file
                value_obj.value = value
                value_obj.save()
        else:
            if value is None or value == '':
                value_obj.delete()
                return
            if value != value_obj.value:
                value_obj.value = value
                value_obj.save()

    def validate_value(self, value):

        # i think that data is already validated

        pass
