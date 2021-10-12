from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewCoachJacketDetailSerializer(serializers.ModelSerializer):
    coach_jac_body_front = ImageDetailSerializer()
    coach_jac_collar_front = ImageDetailSerializer()
    coach_jac_collar_inner_front = ImageDetailSerializer()
    coach_jac_button_front = ImageDetailSerializer()
    coach_jac_left_pocket_front = ImageDetailSerializer()
    coach_jac_right_pocket_front = ImageDetailSerializer()
    coach_jac_hem_front = ImageDetailSerializer()
    coach_jac_left_sleeve_front = ImageDetailSerializer()
    coach_jac_right_sleeve_front = ImageDetailSerializer()
    coach_jac_left_cuff_front = ImageDetailSerializer()
    coach_jac_right_cuff_front = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Front
        fields = ['id', 'name',
                  'coach_jac_body_front',
                  'coach_jac_collar_front',
                  'coach_jac_collar_inner_front',
                  'coach_jac_button_front',
                  'coach_jac_left_pocket_front',
                  'coach_jac_right_pocket_front',
                  'coach_jac_hem_front',
                  'coach_jac_left_sleeve_front',
                  'coach_jac_right_sleeve_front',
                  'coach_jac_left_cuff_front',
                  'coach_jac_right_cuff_front',
                  ]


class BackViewCoachJacketDetailSerializer(serializers.ModelSerializer):
    coach_jac_body_back = ImageDetailSerializer()
    coach_jac_collar_back = ImageDetailSerializer()
    coach_jac_left_sleeve_back = ImageDetailSerializer()
    coach_jac_right_sleeve_back = ImageDetailSerializer()
    coach_jac_hem_back = ImageDetailSerializer()
    coach_jac_left_cuff_back = ImageDetailSerializer()
    coach_jac_right_cuff_back = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Back
        fields = ['id', 'name',
                  'coach_jac_body_back',
                  'coach_jac_collar_back',
                  'coach_jac_left_sleeve_back',
                  'coach_jac_right_sleeve_back',
                  'coach_jac_hem_back',
                  'coach_jac_left_cuff_back',
                  'coach_jac_right_cuff_back',
                  ]


class LeftViewCoachJacketDetailSerializer(serializers.ModelSerializer):
    coach_jac_mid_body_left = ImageDetailSerializer()
    coach_jac_left_body_left = ImageDetailSerializer()
    coach_jac_right_body_left = ImageDetailSerializer()
    coach_jac_bottom_body_left = ImageDetailSerializer()
    coach_jac_mid_cuff_left = ImageDetailSerializer()
    coach_jac_left_cuff_left = ImageDetailSerializer()
    coach_jac_right_cuff_left = ImageDetailSerializer()
    coach_jac_bottom_cuff_left = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Left
        fields = ['id', 'name',
                  'coach_jac_mid_body_left',
                  'coach_jac_left_body_left',
                  'coach_jac_right_body_left',
                  'coach_jac_bottom_body_left',
                  'coach_jac_mid_cuff_left',
                  'coach_jac_left_cuff_left',
                  'coach_jac_right_cuff_left',
                  'coach_jac_bottom_cuff_left',
                  ]


class RightViewCoachJacketDetailSerializer(serializers.ModelSerializer):
    coach_jac_mid_body_right = ImageDetailSerializer()
    coach_jac_left_body_right = ImageDetailSerializer()
    coach_jac_right_body_right = ImageDetailSerializer()
    coach_jac_bottom_body_right = ImageDetailSerializer()
    coach_jac_mid_cuff_right = ImageDetailSerializer()
    coach_jac_left_cuff_right = ImageDetailSerializer()
    coach_jac_right_cuff_right = ImageDetailSerializer()
    coach_jac_bottom_cuff_right = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Right
        fields = ['id', 'name',
                  'coach_jac_mid_body_right',
                  'coach_jac_left_body_right',
                  'coach_jac_right_body_right',
                  'coach_jac_bottom_body_right',
                  'coach_jac_mid_cuff_right',
                  'coach_jac_left_cuff_right',
                  'coach_jac_right_cuff_right',
                  'coach_jac_bottom_cuff_right',
                  ]


# class CoachJacDetailSerializer(serializers.ModelSerializer):
#     front_view = CoachJacFrontSerializer()
#     back_view = CoachJacBackSerializer()
#     left_view = CoachJacLeftSerializer()
#     right_view = CoachJacRightSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view', 'back_view', 'left_view',
#                   'right_view'
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_coach_jac:
#             serializer = CoachJacFrontSerializer(obj.front_view_coach_jac)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_coach_jac:
#             serializer = CoachJacBackSerializer(obj.back_view_coach_jac)
#             return serializer.data
#         else:
#             return None
#
#     def get_right_view(self, obj):
#         if obj.right_view_coach_jac:
#             serializer = CoachJacRightSerializer(obj.right_view_coach_jac)
#             return serializer.data
#         else:
#             return None
#
#     def get_left_view(self, obj):
#         if obj.left_view_coach_jac:
#             serializer = CoachJacLeftSerializer(obj.left_view_coach_jac)
#             return serializer.data
#         else:
#             return None
