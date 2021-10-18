from rest_framework import serializers
from constructor import models


class ProductComponentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ComponentSelection
        fields = ['id', 'category', 'component', 'display_image']
