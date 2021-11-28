from constructor.models import CustomUser, UserOrder
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_no', 'address')


class UserOrderSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = UserOrder
        fields = ('id', 'order_no', 'product', 'quantity', 'total_price', 'payment_done')

    def get_product(self, obj):
        return {'name': obj.product_design.name, }
