from rest_framework import serializers
from constructor import models


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DesignImages
        fields = ['id', 'name', 'image']
