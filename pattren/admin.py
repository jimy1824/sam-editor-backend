from django.contrib import admin
from .models import LogosCategory, PresetLogos, UserLogo
from constructor.models import PrintingMethod, SilkPrintingMethodSizeCostQuantity, \
    HeatTransferPrintingMethodSizeCostQuantity, DigitalPrintingMethodSizeCostQuantity


# Register your models here.
@admin.register(PrintingMethod)
class PrintingMethodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PrintingMethod._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


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


@admin.register(UserLogo)
class PresetLogosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserLogo._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
