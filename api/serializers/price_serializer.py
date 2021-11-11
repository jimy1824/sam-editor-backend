from rest_framework import serializers
from constructor import models


class SilkPrintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SilkPrintingMethodSizeCostQuantity

        fields = ['id', 'name', 'color_type', 'height',
                  'width', 'quantity_to', 'quantity_from',
                  'first_color_cost', 'additional_color_cost',
                  'screen_cost']


class HeatTransferPrintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeatTransferPrintingMethodSizeCostQuantity

        fields = ['id', 'name', 'printing_type', 'height', 'width', 'cost']


class DigitalPrintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DigitalPrintingMethodSizeCostQuantity

        fields = ['id', 'name', 'height', 'width', 'cost']


class PrintingPriceListSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()

    class Meta:
        model = models.PrintingMethod

        fields = ['id', 'printing_method', 'name', 'printing_base_price', 'cost']

    def get_cost(self, obj):
        if obj.printing_method == 'silk_screen':
            serializer = SilkPrintingSerializer(obj.silk_sizes_quantity_cost, many=True)
            return serializer.data

        if obj.printing_method == 'heat_transfer':
            serializer = HeatTransferPrintingSerializer(obj.heat_transfer_sizes_cost, many=True)
            return serializer.data

        if obj.printing_method == 'digital':
            serializer = DigitalPrintingSerializer(obj.digital_sizes_cost, many=True)
            return serializer.data

        return []


class PrintingPriceDetailSerializer(serializers.ModelSerializer):
    model = models.PrintingMethod

    class Meta:
        model = models.PrintingMethod

        fields = ['id', 'name', 'silk_sizes_quantity_cost', 'heat_transfer_sizes_cost', 'digital_sizes_cost',
                  'printing_price']
