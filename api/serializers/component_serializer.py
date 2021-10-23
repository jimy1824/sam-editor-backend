from rest_framework import serializers
from constructor import models
from .product_serializer import ComponentListDetailSerializer


class ProductComponentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ComponentSelection

        fields = ['id', 'category', 'display_image']


class ProductComponentsListSerializer(serializers.ModelSerializer):
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Components

        fields = ['id', 'name', 'designs']

    def get_designs(self, obj):
        category_id = self.context.get('category_id')
        designs = models.ComponentSelection.objects.filter(category__id=category_id, component=obj)
        serializer = ProductComponentListSerializer(designs, many=True)
        return serializer.data


class ProductComponentCategoryNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Components
        fields = ['id', 'name']
