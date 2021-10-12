from rest_framework import serializers
from constructor import models


class ImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()

    class Meta:
        model = models.ImageField
        fields = ['id', 'name', 'image', 'color', 'x_point', 'y_point', 'width', 'height', 'type']

    def get_image(self, obj):
        # return 'http://localhost:8000' + obj.image.url
        return 'http://44.192.67.250' + obj.image.url

    def get_type(self, obj):
        if self.context.get('type'):
            return self.context.get('type')
        return None

    def get_color(self, obj):
        return None
