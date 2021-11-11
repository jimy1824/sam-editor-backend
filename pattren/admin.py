from django.contrib import admin

from .models import LogosCategory, PresetLogos, UserLogo
from constructor.models import PrintingMethod, SilkPrintingMethodSizeCostQuantity, \
    HeatTransferPrintingMethodSizeCostQuantity, DigitalPrintingMethodSizeCostQuantity

from .models import PresetSublimationPatterns, SublimationCategory


# Register your models here.
@admin.register(PrintingMethod)
class PrintingMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'printing_method']
    ordering = ['id']
    search_fields = ('name',)
    change_form_template = 'admin/admin_printing_customization.html'
    # filter_horizontal = ('silk_sizes_quantity_cost', 'digital_sizes_cost', 'heat_transfer_sizes_cost')


@admin.register(SilkPrintingMethodSizeCostQuantity)
class SilkPrintingMethodSizeCostQuantityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SilkPrintingMethodSizeCostQuantity._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(HeatTransferPrintingMethodSizeCostQuantity)
class HeatTransferPrintingMethodSizeCostQuantityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HeatTransferPrintingMethodSizeCostQuantity._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(DigitalPrintingMethodSizeCostQuantity)
class DigitalPrintingMethodSizeCostQuantityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DigitalPrintingMethodSizeCostQuantity._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(LogosCategory)
class LogosCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LogosCategory._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(PresetLogos)
class PresetLogosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PresetLogos._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(SublimationCategory)
class SublimationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SublimationCategory._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(PresetSublimationPatterns)
class PresetSublimationPatternsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PresetSublimationPatterns._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(UserLogo)
class PresetLogosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserLogo._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
