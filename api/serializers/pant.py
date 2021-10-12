from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewPantDetailSerializer(serializers.ModelSerializer):
    pant_upper_waist_front = ImageDetailSerializer()
    pant_lower_waist_front = ImageDetailSerializer()
    pant_thai_left_front = ImageDetailSerializer()
    pant_thai_right_front = ImageDetailSerializer()
    pant_knees_left_front = ImageDetailSerializer()
    pant_knees_right_front = ImageDetailSerializer()
    pant_bottom_left_front = ImageDetailSerializer()
    pant_bottom_right_front = ImageDetailSerializer()
    pant_pocket_left_front = ImageDetailSerializer()
    pant_pocket_right_front = ImageDetailSerializer()

    class Meta:
        model = models.PantFront
        fields = ['id', 'name', 'pant_upper_waist_front', 'pant_lower_waist_front', 'pant_thai_left_front',
                  'pant_thai_right_front', 'pant_knees_left_front', 'pant_knees_right_front',
                  'pant_bottom_left_front',
                  'pant_bottom_right_front',
                  'pant_pocket_left_front',
                  'pant_pocket_right_front']


class BackViewPantDetailSerializer(serializers.ModelSerializer):
    pant_upper_waist_back = ImageDetailSerializer()
    pant_lower_waist_back = ImageDetailSerializer()
    pant_thai_left_back = ImageDetailSerializer()
    pant_thai_right_back = ImageDetailSerializer()
    pant_knees_left_back = ImageDetailSerializer()
    pant_knees_right_back = ImageDetailSerializer()
    pant_bottom_left_back = ImageDetailSerializer()
    pant_bottom_right_back = ImageDetailSerializer()
    pant_pocket_left_back = ImageDetailSerializer()
    pant_pocket_right_back = ImageDetailSerializer()

    class Meta:
        model = models.PantBack
        fields = ['id', 'name', 'pant_upper_waist_back', 'pant_lower_waist_back', 'pant_thai_left_back',
                  'pant_thai_right_back', 'pant_knees_left_back', 'pant_knees_right_back',
                  'pant_bottom_left_back',
                  'pant_bottom_right_back',
                  'pant_pocket_left_back',
                  'pant_pocket_right_back']


# class PantDetailSerializer(serializers.ModelSerializer):
#     front_view = PantFrontDetailSerializer()
#     back_view = PantBackDetailSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view', 'back_view']
#
#     def get_front_view(self, obj):
#         if obj.front_view_pant:
#             serializer = PantFrontDetailSerializer(obj.front_view_pant)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_pant:
#             serializer = PantBackDetailSerializer(obj.back_view_pant)
#             return serializer.data
#         else:
#             return None
