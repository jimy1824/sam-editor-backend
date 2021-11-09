from rest_framework import serializers
from constructor import models
from pattren.models import LogosCategory, PresetLogos, PresetSublimationPatterns, SublimationCategory


class UserLogoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DesignImages
        fields = ['id', 'name', 'image']


# class UserSublimationListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DesignImages
#         fields = ['id', 'name', 'image']


class LogoCategoryListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = LogosCategory
        fields = ['id', 'name', 'selected']

    def get_selected(self, obj):
        return False


class LogoCategoryPatternsListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = PresetSublimationPatterns
        fields = ['id', 'name', 'image', 'selected', 'logo_price']

    def get_selected(self, obj):
        return False


class LogoCategoryDetailSerializer(serializers.ModelSerializer):
    patterns = serializers.SerializerMethodField()

    class Meta:
        model = LogosCategory
        fields = ['id', 'name', 'patterns']

    def get_patterns(self, obj):
        serializer = LogoCategoryPatternsListSerializer(PresetLogos.objects.filter(category=obj),
                                                        context={'request': self.context.get('request')}, many=True)

        return serializer.data

    def get_logo_price(self, obj):
        return PresetLogos.objects.filter(category=obj).first().logo_price


class SublimationCategoryListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = SublimationCategory
        fields = ['id', 'name', 'selected']

    def get_selected(self, obj):
        return False


class SublimationCategoryPatternsListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = PresetSublimationPatterns
        fields = ['id', 'name', 'image', 'selected']

    def get_selected(self, obj):
        return False


class SublimationDetailSerializerWithCategory(serializers.ModelSerializer):
    patterns = serializers.SerializerMethodField()

    class Meta:
        model = SublimationCategory
        fields = ['id', 'name', 'patterns']

    def get_patterns(self, obj):
        # import pdb;pdb.set_trace()
        serializer = SublimationCategoryPatternsListSerializer(PresetSublimationPatterns.objects.filter(category=obj),
                                                               context={'request': self.context.get('request')},
                                                               many=True)
        return serializer.data
