from django.contrib import admin
from .models import PrintingMethod, LogosCategory, PresetLogos


# Register your models here.
@admin.register(PrintingMethod)
class PrintingMethodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PrintingMethod._meta.fields]
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
