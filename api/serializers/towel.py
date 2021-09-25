from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewTowelDetailSerializer(serializers.ModelSerializer):
    towel_front = ImageDetailSerializer()

    class Meta:
        model = models.TowelFront
        fields = ['id', 'name', 'towel_front']


class BackViewTowelDetailSerializer(serializers.ModelSerializer):
    towel_back = ImageDetailSerializer()

    class Meta:
        model = models.TowelBack
        fields = ['id', 'name', 'towel_back']


class TowelDetailSerializer(serializers.ModelSerializer):
    front_view = serializers.SerializerMethodField()
    back_view = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view', 'back_view']

    def get_front_view(self, obj):
        if obj.front_view_towel:
            serializer = TowelFrontDetailSerializer(obj.front_view_towel)
            return serializer.data
        else:
            return None

    def get_back_view(self, obj):
        if obj.back_view_towel:
            serializer = TowelBackDetailSerializer(obj.back_view_towel)
            return serializer.data
        else:
            return None
