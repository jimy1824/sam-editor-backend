from django.contrib import admin
from django.utils.html import format_html

from constructor import models as ConstructorModels
from django import forms


@admin.register(ConstructorModels.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Category._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ProductDesign)
class CategoryProductDesignAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'display_image_tag']
    ordering = ['id']
    search_fields = ('name',)

    def display_image_tag(self, obj):
        return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))


@admin.register(ConstructorModels.Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Body._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ImageField)
class ImageFieldAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.ImageField._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
