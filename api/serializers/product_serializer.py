from rest_framework import serializers
from constructor import models


class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageField
        fields = ['id', 'name', 'image', 'x_point', 'y_point', 'width', 'height']


class BodyDetailSerializer(serializers.ModelSerializer):
    body_view = ImageDetailSerializer()
    body_first_section = ImageDetailSerializer()
    body_second_section = ImageDetailSerializer()
    body_third_section = ImageDetailSerializer()
    collar = ImageDetailSerializer()
    hem = ImageDetailSerializer()

    class Meta:
        model = models.Body
        fields = ['id', 'name', 'body_view', 'body_first_section', 'body_second_section', 'body_third_section',
                  'collar', 'hem']


class ProductDetailSerializer(serializers.ModelSerializer):
    front_view = BodyDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class CategoryListSerializer(serializers.ModelSerializer):
    designs = ProductListSerializer(source='productdesign_set', many=True)

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']
