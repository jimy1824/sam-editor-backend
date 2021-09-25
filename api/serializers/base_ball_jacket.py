from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewBaseBallJacketDetailSerializer(serializers.ModelSerializer):
    base_b_jac_front_body = ImageDetailSerializer()
    base_b_jac_front_collar = ImageDetailSerializer()
    base_b_jac_front_collar_inner = ImageDetailSerializer()
    base_b_jac_front_hem = ImageDetailSerializer()
    base_b_jac_front_hem_strips = ImageDetailSerializer()
    base_b_jac_front_hem_mid = ImageDetailSerializer()
    base_b_jac_front_button_body = ImageDetailSerializer()
    base_b_jac_front_button_hem = ImageDetailSerializer()
    base_b_jac_left_pocket_front = ImageDetailSerializer()
    base_b_jac_right_pocket_front = ImageDetailSerializer()
    base_b_jac_left_sleeve_front = ImageDetailSerializer()
    base_b_jac_left_cuff_front = ImageDetailSerializer()
    base_b_jac_left_cuff_front_strips = ImageDetailSerializer()
    base_b_jac_right_sleeve_front = ImageDetailSerializer()
    base_b_jac_right_cuff_front = ImageDetailSerializer()
    base_b_jac_right_cuff_front_strips = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Front
        fields = ['id', 'name', 'base_b_jac_front_body', 'base_b_jac_front_collar',
                  'base_b_jac_front_collar_inner', 'base_b_jac_front_hem', 'base_b_jac_front_hem_strips',
                  'base_b_jac_front_hem_mid', 'base_b_jac_front_button_body', 'base_b_jac_front_button_hem',
                  'base_b_jac_left_pocket_front', 'base_b_jac_right_pocket_front', 'base_b_jac_left_sleeve_front',
                  'base_b_jac_left_cuff_front', 'base_b_jac_left_cuff_front_strips', 'base_b_jac_right_sleeve_front',
                  'base_b_jac_right_cuff_front', 'base_b_jac_right_cuff_front_strips'
                  ]


class BackViewBaseBallJacketDetailSerializer(serializers.ModelSerializer):
    base_b_jac_collar_back = ImageDetailSerializer()
    base_b_jac_collar_strips_back = ImageDetailSerializer()
    base_b_jac_body_back = ImageDetailSerializer()
    base_b_jac_hem_back = ImageDetailSerializer()
    base_b_jac_hem_strips_back = ImageDetailSerializer()
    base_b_jac_left_sleeve_back = ImageDetailSerializer()
    base_b_jac_left_cuff_back = ImageDetailSerializer()
    base_b_jac_left_cuff_strip_back = ImageDetailSerializer()
    base_b_jac_right_sleeve_back = ImageDetailSerializer()
    base_b_jac_right_cuff_back = ImageDetailSerializer()
    base_b_jac_right_cuff_strip_back = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Back

        fields = ['id', 'name',
                  'base_b_jac_collar_back',
                  'base_b_jac_collar_strips_back',
                  'base_b_jac_body_back',
                  'base_b_jac_hem_back',
                  'base_b_jac_hem_strips_back',
                  'base_b_jac_left_sleeve_back',
                  'base_b_jac_left_cuff_back',
                  'base_b_jac_left_cuff_strip_back',
                  'base_b_jac_right_sleeve_back',
                  'base_b_jac_right_cuff_back',
                  'base_b_jac_right_cuff_strip_back',
                  ]


class LeftViewBaseBallJacketDetailSerializer(serializers.ModelSerializer):
    base_b_jac_mid_body_left = ImageDetailSerializer()
    base_b_jac_mid_cuff_left = ImageDetailSerializer()
    base_b_jac_mid_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_left_body_left = ImageDetailSerializer()
    base_b_jac_left_cuff_left = ImageDetailSerializer()
    base_b_jac_left_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_right_body_left = ImageDetailSerializer()
    base_b_jac_right_cuff_left = ImageDetailSerializer()
    base_b_jac_right_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_bottom_body_left = ImageDetailSerializer()
    base_b_jac_bottom_cuff_left = ImageDetailSerializer()
    base_b_jac_bottom_cuff_strips_left = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Left

        fields = ['id', 'name',
                  'base_b_jac_mid_body_left',
                  'base_b_jac_mid_cuff_left',
                  'base_b_jac_mid_cuff_strips_left',
                  'base_b_jac_left_body_left',
                  'base_b_jac_left_cuff_left',
                  'base_b_jac_left_cuff_strips_left',
                  'base_b_jac_right_body_left',
                  'base_b_jac_right_cuff_left',
                  'base_b_jac_right_cuff_strips_left',
                  'base_b_jac_bottom_body_left',
                  'base_b_jac_bottom_cuff_left',
                  'base_b_jac_bottom_cuff_strips_left',
                  ]


class RightViewBaseBallJacketDetailSerializer(serializers.ModelSerializer):
    base_b_jac_mid_body_right = ImageDetailSerializer()
    base_b_jac_mid_cuff_right = ImageDetailSerializer()
    base_b_jac_mid_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_left_body_right = ImageDetailSerializer()
    base_b_jac_left_cuff_right = ImageDetailSerializer()
    base_b_jac_left_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_right_body_right = ImageDetailSerializer()
    base_b_jac_right_cuff_right = ImageDetailSerializer()
    base_b_jac_right_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_bottom_body_right = ImageDetailSerializer()
    base_b_jac_bottom_cuff_right = ImageDetailSerializer()
    base_b_jac_bottom_cuff_strips_right = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Right
        fields = ['id', 'name',
                  'base_b_jac_mid_body_right',
                  'base_b_jac_mid_cuff_right',
                  'base_b_jac_mid_cuff_strips_right',
                  'base_b_jac_left_body_right',
                  'base_b_jac_left_cuff_right',
                  'base_b_jac_left_cuff_strips_right',
                  'base_b_jac_right_body_right',
                  'base_b_jac_right_cuff_right',
                  'base_b_jac_right_cuff_strips_right',
                  'base_b_jac_bottom_body_right',
                  'base_b_jac_bottom_cuff_right',
                  'base_b_jac_bottom_cuff_strips_right',
                  ]


# class BaseBJacDetailSerializer(serializers.ModelSerializer):
#     front_view = BaseBJacketFrontViewSerializer()
#     back_view = BaseBJacketBackViewSerializer()
#     left_view = BaseBJacketLeftViewSerializer()
#     right_view = BaseBJacketRightViewSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view', 'back_view', 'left_view',
#                   'right_view'
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_base_b_jacket:
#             serializer = BaseBJacketFrontViewSerializer(obj.front_view_base_b_jacket)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_base_b_jacket:
#             serializer = BaseBJacketBackViewSerializer(obj.back_view_base_b_jacket)
#             return serializer.data
#         else:
#             return None
#
#     def get_right_view(self, obj):
#         if obj.right_view_base_b_jacket:
#             serializer = BaseBJacketRightViewSerializer(obj.right_view_base_b_jacket)
#             return serializer.data
#         else:
#             return None
#
#     def get_left_view(self, obj):
#         if obj.left_view_base_b_jacket:
#             serializer = BaseBJacketLeftViewSerializer(obj.left_view_base_b_jacket)
#             return serializer.data
#         else:
#             return None

