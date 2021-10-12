from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewHatDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_front = ImageDetailSerializer()
    hat_dot_right_front = ImageDetailSerializer()
    hat_upper_part_front = ImageDetailSerializer()
    hat_lower_part_front = ImageDetailSerializer()
    hat_top_button_front = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_front', 'hat_dot_right_front', 'hat_upper_part_front',
                  'hat_lower_part_front', 'hat_top_button_front']


class BackViewHatDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_back = ImageDetailSerializer()
    hat_dot_right_back = ImageDetailSerializer()
    hat_upper_part_back = ImageDetailSerializer()
    hat_lower_strip_back = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_back', 'hat_dot_right_back', 'hat_upper_part_back',
                  'hat_lower_strip_back']


class LeftViewHatDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_left = ImageDetailSerializer()
    hat_dot_right_left = ImageDetailSerializer()
    hat_upper_part_left = ImageDetailSerializer()
    hat_lower_part_left = ImageDetailSerializer()
    hat_top_button_left = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_left', 'hat_dot_right_left', 'hat_upper_part_left',
                  'hat_lower_part_left', 'hat_top_button_left']


class RightViewHatDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_right = ImageDetailSerializer()
    hat_dot_right_right = ImageDetailSerializer()
    hat_upper_part_right = ImageDetailSerializer()
    hat_lower_part_right = ImageDetailSerializer()
    hat_top_button_right = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_right', 'hat_dot_right_right', 'hat_upper_part_right',
                  'hat_lower_part_right', 'hat_top_button_right']


# class HatDetailSerializer(serializers.ModelSerializer):
#     front_view_hat = HatFrontDetailSerializer()
#     back_view_hat = HatBackDetailSerializer()
#     left_view_hat = HatLeftDetailSerializer()
#     right_view_hat = HatRightDetailSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view_hat', 'back_view_hat', 'left_view_hat', 'right_view_hat']
