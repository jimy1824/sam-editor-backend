from rest_framework import serializers
from constructor import models


class ProductPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrintingMethod

        fields = ['id', 'name', 'silk_sizes_quantity_cost', 'heat_transfer_sizes_cost', 'digital_sizes_cost']
