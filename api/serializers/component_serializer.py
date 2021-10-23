from rest_framework import serializers
from constructor import models
from .product_serializer import ComponentListDetailSerializer


class ProductComponentListSerializer(serializers.ModelSerializer):

    component = ComponentListDetailSerializer()

    class Meta:
        model = models.ComponentSelection

        fields = ['id', 'category', 'component', 'display_image']


class ProductComponentCategoryNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Components
        fields = ['id', 'name']
