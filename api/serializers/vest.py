from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewVestDetailSerializer(serializers.ModelSerializer):
    collar_vest = ImageDetailSerializer()
    zip_vest = ImageDetailSerializer()
    vest_top = ImageDetailSerializer()
    vest_mid = ImageDetailSerializer()
    vest_bottom = ImageDetailSerializer()
    vest_pocket_left = ImageDetailSerializer()
    vest_pocket_right = ImageDetailSerializer()
    vest_hem = ImageDetailSerializer()
    vest_left_sleeve = ImageDetailSerializer()
    vest_right_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.VestFront
        fields = ['id', 'name', 'collar_vest', 'zip_vest', 'vest_top',
                  'vest_mid', 'vest_bottom', 'vest_pocket_right',
                  'vest_pocket_left', 'vest_hem', 'vest_left_sleeve', 'vest_right_sleeve']


class BackViewVestDetailSerializer(serializers.ModelSerializer):
    collar_vest_back = ImageDetailSerializer()
    vest_top_back = ImageDetailSerializer()
    vest_mid_back = ImageDetailSerializer()
    vest_bottom_back = ImageDetailSerializer()
    vest_pocket_left_back = ImageDetailSerializer()
    vest_pocket_right_back = ImageDetailSerializer()
    vest_hem_back = ImageDetailSerializer()
    vest_left_sleeve_back = ImageDetailSerializer()
    vest_right_sleeve_back = ImageDetailSerializer()

    class Meta:
        model = models.VestBack
        fields = ['id', 'name', 'collar_vest_back', 'vest_top_back', 'vest_mid_back',
                  'vest_bottom_back', 'vest_pocket_left_back', 'vest_pocket_right_back', 'vest_hem_back',
                  'vest_left_sleeve_back', 'vest_right_sleeve_back']


# class VestDetailSerializer(serializers.ModelSerializer):
#     front_view = VestFrontDetailSerializer()
#     back_view = VestBackDetailSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view', 'back_view']
#
#     def get_front_view(self, obj):
#         if obj.front_view_vest:
#             serializer = VestFrontDetailSerializer(obj.front_view_vest)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_vest:
#             serializer = VestBackDetailSerializer(obj.back_view_vest)
#             return serializer.data
#         else:
#             return None
