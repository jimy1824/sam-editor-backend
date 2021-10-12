from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewApronDetailSerializer(serializers.ModelSerializer):
    collar_strip = ImageDetailSerializer()
    collar_strip_side = ImageDetailSerializer()
    bukkle = ImageDetailSerializer()
    appren_body = serializers.SerializerMethodField()
    left_strip = ImageDetailSerializer()
    right_strip = ImageDetailSerializer()
    pocket = ImageDetailSerializer()

    class Meta:
        model = models.Apron
        fields = ['id', 'name', 'collar_strip', 'collar_strip_side', 'bukkle', 'appren_body', 'left_strip',
                  'right_strip',
                  'pocket']

    def get_appren_body(self, obj):
        serializer = ImageDetailSerializer(obj.body)
        return serializer.data


# class ApronDetailSerializer(serializers.ModelSerializer):
#     front_view_apron = ApronFrontDetailSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name', 'front_view_apron']