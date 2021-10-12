from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewHoodieDetailSerializer(serializers.ModelSerializer):
    cap_left = ImageDetailSerializer()
    cap_right = ImageDetailSerializer()
    cap_inner_mid = ImageDetailSerializer()
    cap_inner_left = ImageDetailSerializer()
    cap_inner_right = ImageDetailSerializer()
    cap_inner_bottom = ImageDetailSerializer()
    hood_left_strip = ImageDetailSerializer()
    hood_right_strip = ImageDetailSerializer()
    zip = ImageDetailSerializer()
    hood_top = ImageDetailSerializer()
    hood_top_left = ImageDetailSerializer()
    hood_top_right = ImageDetailSerializer()
    hood_mid = ImageDetailSerializer()
    hood_mid_left = ImageDetailSerializer()
    hood_mid_right = ImageDetailSerializer()
    hood_bottom = ImageDetailSerializer()
    hood_bottom_left = ImageDetailSerializer()
    hood_bottom_right = ImageDetailSerializer()
    hood_hem_left = ImageDetailSerializer()
    hood_hem_right = ImageDetailSerializer()
    hood_left_sleeve_full = ImageDetailSerializer()
    hood_left_sleeve_top = ImageDetailSerializer()
    hood_left_sleeve_mid = ImageDetailSerializer()
    hood_left_sleeve_bottom = ImageDetailSerializer()
    hood_left_sleeve_cuff = ImageDetailSerializer()
    hood_left_sleeve_cuff_strips = ImageDetailSerializer()
    hood_right_sleeve_full = ImageDetailSerializer()
    hood_right_sleeve_top = ImageDetailSerializer()
    hood_right_sleeve_mid = ImageDetailSerializer()
    hood_right_sleeve_bottom = ImageDetailSerializer()
    hood_right_sleeve_cuff = ImageDetailSerializer()
    hood_right_sleeve_cuff_strips = ImageDetailSerializer()

    class Meta:
        model = models.HoodieFront
        fields = ['id', 'name',
                  'cap_left',
                  'cap_right',
                  'cap_inner_mid',
                  'cap_inner_left',
                  'cap_inner_right',
                  'cap_inner_bottom',
                  'hood_left_strip',
                  'hood_right_strip',
                  'zip',
                  'hood_top',
                  'hood_top_left',
                  'hood_top_right',
                  'hood_mid',
                  'hood_mid_left',
                  'hood_mid_right',
                  'hood_bottom',
                  'hood_bottom_left',
                  'hood_bottom_right',
                  'hood_hem_left',
                  'hood_hem_right',
                  'hood_left_sleeve_full',
                  'hood_left_sleeve_top',
                  'hood_left_sleeve_mid',
                  'hood_left_sleeve_bottom',
                  'hood_left_sleeve_cuff',
                  'hood_left_sleeve_cuff_strips',
                  'hood_right_sleeve_full',
                  'hood_right_sleeve_top',
                  'hood_right_sleeve_mid',
                  'hood_right_sleeve_bottom',
                  'hood_right_sleeve_cuff',
                  'hood_right_sleeve_cuff_strips',
                  ]


class BackViewHoodieDetailSerializer(serializers.ModelSerializer):
    cap_left_back = ImageDetailSerializer()
    cap_right_back = ImageDetailSerializer()
    hood_top_back = ImageDetailSerializer()
    hood_top_left_back = ImageDetailSerializer()
    hood_top_right_back = ImageDetailSerializer()
    hood_mid_back = ImageDetailSerializer()
    hood_mid_left_back = ImageDetailSerializer()
    hood_mid_right_back = ImageDetailSerializer()
    hood_bottom_back = ImageDetailSerializer()
    hood_bottom_left_back = ImageDetailSerializer()
    hood_bottom_right_back = ImageDetailSerializer()
    hood_hem_back = ImageDetailSerializer()
    hood_left_sleeve_full_back = ImageDetailSerializer()
    hood_left_sleeve_top_back = ImageDetailSerializer()
    hood_left_sleeve_mid_back = ImageDetailSerializer()
    hood_left_sleeve_bottom_back = ImageDetailSerializer()
    hood_left_sleeve_cuff_back = ImageDetailSerializer()
    hood_left_sleeve_cuff_strips_back = ImageDetailSerializer()
    hood_right_sleeve_full_back = ImageDetailSerializer()
    hood_right_sleeve_top_back = ImageDetailSerializer()
    hood_right_sleeve_mid_back = ImageDetailSerializer()
    hood_right_sleeve_bottom_back = ImageDetailSerializer()
    hood_right_sleeve_cuff_back = ImageDetailSerializer()
    hood_right_sleeve_cuff_strips_back = ImageDetailSerializer()

    class Meta:
        model = models.HoodieBack
        fields = ['id', 'name',
                  'cap_left_back',
                  'cap_right_back',
                  'hood_top_back',
                  'hood_top_left_back',
                  'hood_top_right_back',
                  'hood_mid_back',
                  'hood_mid_left_back',
                  'hood_mid_right_back',
                  'hood_bottom_back',
                  'hood_bottom_left_back',
                  'hood_bottom_right_back',
                  'hood_hem_back',
                  'hood_left_sleeve_full_back',
                  'hood_left_sleeve_top_back',
                  'hood_left_sleeve_mid_back',
                  'hood_left_sleeve_bottom_back',
                  'hood_left_sleeve_cuff_back',
                  'hood_left_sleeve_cuff_strips_back',
                  'hood_right_sleeve_full_back',
                  'hood_right_sleeve_top_back',
                  'hood_right_sleeve_mid_back',
                  'hood_right_sleeve_bottom_back',
                  'hood_right_sleeve_cuff_back',
                  'hood_right_sleeve_cuff_strips_back',
                  ]


class LeftViewHoodieDetailSerializer(serializers.ModelSerializer):
    mid_full_body_hoodie_left = ImageDetailSerializer()
    mid_top_hoodie_left = ImageDetailSerializer()
    mid_mid_hoodie_left = ImageDetailSerializer()
    mid_bottom_hoodie_left = ImageDetailSerializer()
    mid_cuff_hoodie_left = ImageDetailSerializer()
    mid_cuff_strips_hoodie_left = ImageDetailSerializer()
    left_full_body_hoodie_left = ImageDetailSerializer()
    left_top_hoodie_left = ImageDetailSerializer()
    left_mid_hoodie_left = ImageDetailSerializer()
    left_bottom_hoodie_left = ImageDetailSerializer()
    left_cuff_hoodie_left = ImageDetailSerializer()
    left_cuff_strips_hoodie_left = ImageDetailSerializer()
    right_full_body_hoodie_left = ImageDetailSerializer()
    right_top_hoodie_left = ImageDetailSerializer()
    right_mid_hoodie_left = ImageDetailSerializer()
    right_bottom_hoodie_left = ImageDetailSerializer()
    right_cuff_hoodie_left = ImageDetailSerializer()
    right_cuff_strips_hoodie_left = ImageDetailSerializer()
    bottom_full_body_hoodie_left = ImageDetailSerializer()
    bottom_top_hoodie_left = ImageDetailSerializer()
    bottom_mid_hoodie_left = ImageDetailSerializer()
    bottom_bottom_hoodie_left = ImageDetailSerializer()
    bottom_cuff_hoodie_left = ImageDetailSerializer()
    bottom_cuff_strips_hoodie_left = ImageDetailSerializer()

    class Meta:
        model = models.HoodieLeft
        fields = ['id', 'name',
                  'mid_full_body_hoodie_left',
                  'mid_top_hoodie_left',
                  'mid_mid_hoodie_left',
                  'mid_bottom_hoodie_left',
                  'mid_cuff_hoodie_left',
                  'mid_cuff_strips_hoodie_left',
                  'left_full_body_hoodie_left',
                  'left_top_hoodie_left',
                  'left_mid_hoodie_left',
                  'left_bottom_hoodie_left',
                  'left_cuff_hoodie_left',
                  'left_cuff_strips_hoodie_left',
                  'right_full_body_hoodie_left',
                  'right_top_hoodie_left',
                  'right_mid_hoodie_left',
                  'right_bottom_hoodie_left',
                  'right_cuff_hoodie_left',
                  'right_cuff_strips_hoodie_left',
                  'bottom_full_body_hoodie_left',
                  'bottom_top_hoodie_left',
                  'bottom_mid_hoodie_left',
                  'bottom_bottom_hoodie_left',
                  'bottom_cuff_hoodie_left',
                  'bottom_cuff_strips_hoodie_left',
                  ]


class RightViewHoodieDetailSerializer(serializers.ModelSerializer):
    mid_full_body_hoodie_right = ImageDetailSerializer()
    mid_top_hoodie_right = ImageDetailSerializer()
    mid_mid_hoodie_right = ImageDetailSerializer()
    mid_bottom_hoodie_right = ImageDetailSerializer()
    mid_cuff_hoodie_right = ImageDetailSerializer()
    mid_cuff_strips_hoodie_right = ImageDetailSerializer()
    left_full_body_hoodie_right = ImageDetailSerializer()
    left_top_hoodie_right = ImageDetailSerializer()
    left_mid_hoodie_right = ImageDetailSerializer()
    left_bottom_hoodie_right = ImageDetailSerializer()
    left_cuff_hoodie_right = ImageDetailSerializer()
    left_cuff_strips_hoodie_right = ImageDetailSerializer()
    right_full_body_hoodie_right = ImageDetailSerializer()
    right_top_hoodie_right = ImageDetailSerializer()
    right_mid_hoodie_right = ImageDetailSerializer()
    right_bottom_hoodie_right = ImageDetailSerializer()
    right_cuff_hoodie_right = ImageDetailSerializer()
    right_cuff_strips_hoodie_right = ImageDetailSerializer()
    bottom_full_body_hoodie_right = ImageDetailSerializer()
    bottom_top_hoodie_right = ImageDetailSerializer()
    bottom_mid_hoodie_right = ImageDetailSerializer()
    bottom_bottom_hoodie_right = ImageDetailSerializer()
    bottom_cuff_hoodie_right = ImageDetailSerializer()
    bottom_cuff_strips_hoodie_right = ImageDetailSerializer()

    class Meta:
        model = models.HoodieRight
        fields = ['id', 'name',
                  'mid_full_body_hoodie_right',
                  'mid_top_hoodie_right',
                  'mid_mid_hoodie_right',
                  'mid_bottom_hoodie_right',
                  'mid_cuff_hoodie_right',
                  'mid_cuff_strips_hoodie_right',
                  'left_full_body_hoodie_right',
                  'left_top_hoodie_right',
                  'left_mid_hoodie_right',
                  'left_bottom_hoodie_right',
                  'left_cuff_hoodie_right',
                  'left_cuff_strips_hoodie_right',
                  'right_full_body_hoodie_right',
                  'right_top_hoodie_right',
                  'right_mid_hoodie_right',
                  'right_bottom_hoodie_right',
                  'right_cuff_hoodie_right',
                  'right_cuff_strips_hoodie_right',
                  'bottom_full_body_hoodie_right',
                  'bottom_top_hoodie_right',
                  'bottom_mid_hoodie_right',
                  'bottom_bottom_hoodie_right',
                  'bottom_cuff_hoodie_right',
                  'bottom_cuff_strips_hoodie_right',
                  ]


# class HoodieDetailSerializer(serializers.ModelSerializer):
#     front_view = HoodieFrontSerializer()
#     back_view = HoodieBackSerializer()
#     left_view = HoodieLeftSerializer()
#     right_view = HoodieRightSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name',
#                   'front_view_hoodie',
#                   'back_view_hoodie',
#                   'left_view_hoodie',
#                   'right_view_hoodie'
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_hoodie:
#             serializer = HoodieFrontSerializer(obj.front_view_hoodie)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_hoodie:
#             serializer = HoodieBackSerializer(obj.back_view_hoodie)
#             return serializer.data
#         else:
#             return None
#
#     def get_right_view(self, obj):
#         if obj.right_view_hoodie:
#             serializer = HoodieRightSerializer(obj.right_view_hoodie)
#             return serializer.data
#         else:
#             return None
#
#     def get_left_view(self, obj):
#         if obj.left_view_hoodie:
#             serializer = HoodieLeftSerializer(obj.left_view_hoodie)
#             return serializer.data
#         else:
#             return None
