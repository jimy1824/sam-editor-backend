from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer

class FrontViewBomberJacketDetailSerializer(serializers.ModelSerializer):
    bomber_jac_body_front = ImageDetailSerializer()
    bomber_jac_collar_front = ImageDetailSerializer()
    bomber_jac_collar_inner_front = ImageDetailSerializer()
    bomber_jac_left_pocket_front = ImageDetailSerializer()
    bomber_jac_right_pocket_front = ImageDetailSerializer()
    bomber_jac_left_sleeve_front = ImageDetailSerializer()
    bomber_jac_right_sleeve_front = ImageDetailSerializer()
    bomber_jac_left_cuff_front = ImageDetailSerializer()
    bomber_jac_right_cuff_front = ImageDetailSerializer()
    bomber_jac_right_sleeve_design_front = ImageDetailSerializer()
    bomber_jac_hem_front = ImageDetailSerializer()
    bomber_jac_zip_front = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Front
        fields = ['id', 'name',
                  'bomber_jac_body_front',
                  'bomber_jac_collar_front',
                  'bomber_jac_collar_inner_front',
                  'bomber_jac_left_pocket_front',
                  'bomber_jac_right_pocket_front',
                  'bomber_jac_left_sleeve_front',
                  'bomber_jac_right_sleeve_front',
                  'bomber_jac_left_cuff_front',
                  'bomber_jac_right_cuff_front',
                  'bomber_jac_right_sleeve_design_front',
                  'bomber_jac_hem_front',
                  'bomber_jac_zip_front',

                  ]


class BackViewBomberJacketDetailSerializer(serializers.ModelSerializer):
    bomber_jac_body_back = ImageDetailSerializer()
    bomber_jac_collar_back = ImageDetailSerializer()
    bomber_jac_hem_back = ImageDetailSerializer()
    bomber_jac_left_sleeve_back = ImageDetailSerializer()
    bomber_jac_right_sleeve_back = ImageDetailSerializer()
    bomber_jac_left_cuff_back = ImageDetailSerializer()
    bomber_jac_right_cuff_back = ImageDetailSerializer()
    bomber_jac_left_sleeve_design_back = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Back
        fields = ['id', 'name',
                  'bomber_jac_body_back',
                  'bomber_jac_collar_back',
                  'bomber_jac_hem_back',
                  'bomber_jac_left_sleeve_back',
                  'bomber_jac_right_sleeve_back',
                  'bomber_jac_left_cuff_back',
                  'bomber_jac_right_cuff_back',
                  'bomber_jac_left_sleeve_design_back',
                  ]


class LeftViewBomberJacketDetailSerializer(serializers.ModelSerializer):
    bomber_jac_mid_body_left = ImageDetailSerializer()
    bomber_jac_left_body_left = ImageDetailSerializer()
    bomber_jac_right_body_left = ImageDetailSerializer()
    bomber_jac_bottom_body_left = ImageDetailSerializer()
    bomber_jac_left_cuff_left = ImageDetailSerializer()
    bomber_jac_right_cuff_left = ImageDetailSerializer()
    bomber_jac_mid_cuff_left = ImageDetailSerializer()
    bomber_jac_bottom_cuff_left = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Left
        fields = ['id', 'name',
                  'bomber_jac_mid_body_left',
                  'bomber_jac_left_body_left',
                  'bomber_jac_right_body_left',
                  'bomber_jac_bottom_body_left',
                  'bomber_jac_left_cuff_left',
                  'bomber_jac_right_cuff_left',
                  'bomber_jac_mid_cuff_left',
                  'bomber_jac_bottom_cuff_left',
                  ]


class RightViewBomberJacketDetailSerializer(serializers.ModelSerializer):
    bomber_jac_mid_body_right = ImageDetailSerializer()
    bomber_jac_left_body_right = ImageDetailSerializer()
    bomber_jac_right_body_right = ImageDetailSerializer()
    bomber_jac_bottom_body_right = ImageDetailSerializer()
    bomber_jac_left_cuff_right = ImageDetailSerializer()
    bomber_jac_right_cuff_right = ImageDetailSerializer()
    bomber_jac_mid_cuff_right = ImageDetailSerializer()
    bomber_jac_bottom_cuff_right = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Right
        fields = ['id', 'name',
                  'bomber_jac_mid_body_right',
                  'bomber_jac_left_body_right',
                  'bomber_jac_right_body_right',
                  'bomber_jac_bottom_body_right',
                  'bomber_jac_left_cuff_right',
                  'bomber_jac_right_cuff_right',
                  'bomber_jac_mid_cuff_right',
                  'bomber_jac_bottom_cuff_right',
                  ]


# class BomberJacDetailSerializer(serializers.ModelSerializer):
#     front_view = BomberJacFrontSerializer()
#     back_view = BomberJacBackSerializer()
#     left_view = BomberJacLeftSerializer()
#     right_view = BomberJacRightSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name',
#                   'front_view',
#                   'back_view',
#                   'left_view',
#                   'right_view'
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_base_b_shirt:
#             serializer = BaseBShirtFrontDetailSerializer(obj.front_view_base_b_shirt)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_base_b_shirt:
#             serializer = BaseBShirtBackDetailSerializer(obj.back_view_base_b_shirt)
#             return serializer.data
#         else:
#             return None
#
#     def get_right_view(self, obj):
#         if obj.right_view_base_b_shirt:
#             serializer = BaseBShirtRightDetailSerializer(obj.right_view_base_b_shirt)
#             return serializer.data
#         else:
#             return None
#
#     def get_left_view(self, obj):
#         if obj.left_view_base_b_shirt:
#             serializer = BaseBShirtLeftDetailSerializer(obj.left_view_base_b_shirt)
#             return serializer.data
#         else:
#             return None
