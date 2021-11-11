from rest_framework import serializers
from constructor import models


class PrintingPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrintingMethod

        fields = ['SILK_SCREEN', 'HEAT_TRANSFER', 'DIGITAL']


class PrintingPriceDetailSerializer(serializers.ModelSerializer):
    model = models.PrintingMethod

    class Meta:
        model = models.PrintingMethod

        fields = ['id', 'name', 'silk_sizes_quantity_cost', 'heat_transfer_sizes_cost', 'digital_sizes_cost',
        'printing_price']
