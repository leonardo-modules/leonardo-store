from django.contrib import admin
from brand import models
from django.conf import settings


class BrandTranslationInline(admin.TabularInline):
    model = models.BrandTranslation
    max_num = len(settings.LANGUAGES)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'name', 'description', 'country', ]
    list_filter = ['country']
    inlines = [BrandTranslationInline, ]
    search_fields = ['name', 'description']

admin.site.register(models.Brand, BrandAdmin)
