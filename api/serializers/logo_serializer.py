from rest_framework import serializers
from constructor import models
from pattren.models import LogosCategory, PresetLogos


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DesignImages
        fields = ['id', 'name', 'image']


class LogoCategoryListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = LogosCategory
        fields = ['id', 'name', 'selected']

    def get_selected(self, obj):
        return False


class SublimationPatternsListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = PresetLogos
        fields = ['id', 'name', 'image', 'selected']

    def get_selected(self, obj):
        return False


class LogoCategoryDetailSerializer(serializers.ModelSerializer):
    patterns = serializers.SerializerMethodField()

    class Meta:
        model = LogosCategory
        fields = ['id', 'name', 'patterns']

    def get_patterns(self, obj):
        serializer = SublimationPatternsListSerializer(PresetLogos.objects.filter(category=obj),
                                                       context={'request': self.context.get('request')}, many=True)
        return serializer.data
