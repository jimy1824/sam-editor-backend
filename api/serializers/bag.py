from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewBagDetailSerializer(serializers.ModelSerializer):
    bag_handle_front = ImageDetailSerializer()
    bag_full_front_body = ImageDetailSerializer()
    bag_top_front_body = ImageDetailSerializer()
    bag_mid_front_body = ImageDetailSerializer()
    bag_bottom_front_body = ImageDetailSerializer()

    class Meta:
        model = models.BagFront
        fields = ['id', 'name', 'bag_handle_front', 'bag_full_front_body', 'bag_top_front_body', 'bag_mid_front_body',
                  'bag_bottom_front_body']


class BackViewBagDetailSerializer(serializers.ModelSerializer):
    bag_handle_back = ImageDetailSerializer()
    bag_full_back_body = ImageDetailSerializer()
    bag_top_back_body = ImageDetailSerializer()
    bag_mid_back_body = ImageDetailSerializer()
    bag_bottom_back_body = ImageDetailSerializer()

    class Meta:
        model = models.BagBack
        fields = ['id', 'name', 'bag_handle_back', 'bag_full_back_body', 'bag_top_back_body', 'bag_mid_back_body',
                  'bag_bottom_back_body']


# class BagDetailSerializer(serializers.ModelSerializer):
#     front_view = BagFrontSerializer()
#     back_view = BagBackSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name',
#                   'front_view_bag',
#                   'back_view_bag',
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_bag:
#             serializer = BagFrontSerializer(obj.front_view_bag)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.back_view_bag:
#             serializer = BagBackSerializer(obj.back_view_bag)
#             return serializer.data
#         else:
#             return None
