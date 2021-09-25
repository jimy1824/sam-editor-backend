from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewShirtDetailSerializer(serializers.ModelSerializer):
    body_view = ImageDetailSerializer()
    body_first_section = ImageDetailSerializer()
    body_second_section = ImageDetailSerializer()
    body_third_section = ImageDetailSerializer()
    collar = ImageDetailSerializer()
    hem = ImageDetailSerializer()
    right_sleeve = ImageDetailSerializer(context={'type': 'sleeve'})
    left_sleeve = ImageDetailSerializer(context={'type': 'sleeve'})

    class Meta:
        model = models.Body
        fields = ['id', 'name', 'body_view', 'body_first_section', 'body_second_section', 'body_third_section',
                  'collar', 'hem', 'right_sleeve', 'left_sleeve']


class LeftViewShirtSerializer(serializers.ModelSerializer):
    left_v_body_view = ImageDetailSerializer()
    left_v_upper_part = ImageDetailSerializer()
    left_v_lower_part = ImageDetailSerializer()
    left_v_left_s_upper = ImageDetailSerializer()
    left_v_left_s_lower = ImageDetailSerializer()
    left_v_right_s_upper = ImageDetailSerializer()
    left_v_right_s_lower = ImageDetailSerializer()

    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'left_v_body_view', 'left_v_upper_part', 'left_v_lower_part', 'left_v_left_s_upper',
                  'left_v_left_s_lower', 'left_v_right_s_upper', 'left_v_right_s_lower']


class RightViewShirtSerializer(serializers.ModelSerializer):
    right_v_body_view = ImageDetailSerializer()
    right_v_upper_part = ImageDetailSerializer()
    right_v_lower_part = ImageDetailSerializer()
    right_v_left_s_upper = ImageDetailSerializer()
    right_v_left_s_lower = ImageDetailSerializer()
    right_v_right_s_upper = ImageDetailSerializer()
    right_v_right_s_lower = ImageDetailSerializer()

    class Meta:
        model = models.RightView
        fields = ['id', 'name', 'right_v_body_view', 'right_v_upper_part', 'right_v_lower_part', 'right_v_left_s_upper',
                  'right_v_left_s_lower', 'right_v_right_s_upper', 'right_v_right_s_lower']


class BackViewShirtSerializer(serializers.ModelSerializer):
    back_first_part = ImageDetailSerializer()
    back_second_part = ImageDetailSerializer()
    back_third_part = ImageDetailSerializer()
    back_left_sleeve = serializers.SerializerMethodField()
    back_right_sleeve = serializers.SerializerMethodField()

    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'back_first_part', 'back_second_part', 'back_third_part', 'back_left_sleeve',
                  'back_right_sleeve']

    def get_back_left_sleeve(self, obj):
        serializer = ImageDetailSerializer(obj.back_left_sleeve, context={'type': 'sleeve'})
        return serializer.data

    def get_back_right_sleeve(self, obj):
        serializer = ImageDetailSerializer(obj.back_right_sleeve, context={'type': 'sleeve'})
        return serializer.data
