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
    right_sleeve = ImageDetailSerializer()
    left_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.Body
        fields = ['id', 'name', 'body_view', 'body_first_section', 'body_second_section', 'body_third_section',
                  'collar', 'hem', 'right_sleeve', 'left_sleeve']


class LeftViewSerializer(serializers.ModelSerializer):
    left_v_body_view = ImageDetailSerializer()
    left_v_upper_part = ImageDetailSerializer()
    left_v_lower_part = ImageDetailSerializer()
    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'left_v_upper_part', 'left_v_lower_part']

class RightViewSerializer(serializers.ModelSerializer):
    right_v_body_view = ImageDetailSerializer()
    right_v_upper_part = ImageDetailSerializer()
    right_v_lower_part = ImageDetailSerializer()
    class Meta:
        model = models.RightView
        fields = ['id', 'name', 'right_v_upper_part', 'right_v_lower_part']

class BackViewSerializer(serializers.ModelSerializer):
    back_first_part = ImageDetailSerializer()
    back_second_part = ImageDetailSerializer()
    back_third_part = ImageDetailSerializer()
    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'back_first_part', 'back_second_part', 'back_third_part']


class ProductDetailSerializer(serializers.ModelSerializer):
    front_view = BodyDetailSerializer()
    left_view = LeftViewSerializer()
    right_view = RightViewSerializer()
    back_view = BackViewSerializer()


    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view', 'left_view', 'right_view', 'back_view']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class CategoryListSerializer(serializers.ModelSerializer):
    designs = ProductListSerializer(source='productdesign_set', many=True)

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']
