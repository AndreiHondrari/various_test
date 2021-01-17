from django import forms
from django.contrib import admin

from ajax_select.fields import AutoCompleteSelectField

from . import lookup
from .models import Country, Region, Address


class RegionAdmin(admin.ModelAdmin):
    fields = ('name', 'country')
    list_display = fields
    list_display_links = fields


class RegionTabularInlineAdmin(admin.TabularInline):
    model = Region
    fields = ('name', 'country')


class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields
    list_display_links = fields
    inlines = [
        RegionTabularInlineAdmin,
    ]


class AddressModelForm(forms.ModelForm):

    region = AutoCompleteSelectField('regions')

    class Meta:
        model = Address
        fields = ('name', 'country', 'region',)


class AddressAdmin(admin.ModelAdmin):
    form = AddressModelForm
    list_display = ('name', 'country', 'region',)
    list_display_links = list_display

admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Address, AddressAdmin)
