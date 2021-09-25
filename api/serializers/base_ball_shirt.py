from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewBaseBallShirtDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_body_front = ImageDetailSerializer()
    base_b_shirt_neck_front = ImageDetailSerializer()
    base_b_shirt_left_sleeve_front = ImageDetailSerializer()
    base_b_shirt_right_sleeve_front = ImageDetailSerializer()
    base_b_shirt_button_front = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Front
        fields = ['id', 'name',
                  'base_b_shirt_body_front',
                  'base_b_shirt_neck_front',
                  'base_b_shirt_left_sleeve_front',
                  'base_b_shirt_right_sleeve_front',
                  'base_b_shirt_button_front',
                  ]


class BackViewBaseBallShirtDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_body_back = ImageDetailSerializer()
    base_b_shirt_left_sleeve_back = ImageDetailSerializer()
    base_b_shirt_right_sleeve_back = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Back
        fields = ['id', 'name',
                  'base_b_shirt_body_back',
                  'base_b_shirt_left_sleeve_back',
                  'base_b_shirt_right_sleeve_back',
                  ]


class LeftViewBaseBallShirtDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_mid_left = ImageDetailSerializer()
    base_b_shirt_left_sleeve_left = ImageDetailSerializer()
    base_b_shirt_right_sleeve_left = ImageDetailSerializer()
    base_b_shirt_bottom_sleeve_left = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Left
        fields = ['id', 'name',
                  'base_b_shirt_mid_left',
                  'base_b_shirt_left_sleeve_left',
                  'base_b_shirt_right_sleeve_left',
                  'base_b_shirt_bottom_sleeve_left',
                  ]


class RightViewBaseBallShirtDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_mid_right = ImageDetailSerializer()
    base_b_shirt_left_sleeve_right = ImageDetailSerializer()
    base_b_shirt_right_sleeve_right = ImageDetailSerializer()
    base_b_shirt_bottom_sleeve_right = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Right
        fields = ['id', 'name',
                  'base_b_shirt_mid_right',
                  'base_b_shirt_left_sleeve_right',
                  'base_b_shirt_right_sleeve_right',
                  'base_b_shirt_bottom_sleeve_right',
                  ]


# class BaseBShirtDetailSerializer(serializers.ModelSerializer):
#     front_view = BaseBShirtFrontDetailSerializer()
#     back_view = BaseBShirtBackDetailSerializer()
#     left_view = BaseBShirtLeftDetailSerializer()
#     right_view = BaseBShirtRightDetailSerializer()
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
