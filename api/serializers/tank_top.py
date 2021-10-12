from rest_framework import serializers
from constructor import models
from .common import ImageDetailSerializer


class FrontViewTankTopDetailSerializer(serializers.ModelSerializer):
    tank_collar_front = ImageDetailSerializer()
    tank_collar_inner_front = ImageDetailSerializer()
    tank_top_front = ImageDetailSerializer()
    tank_mid_front = ImageDetailSerializer()
    tank_bottom_front = ImageDetailSerializer()
    tank_left_sleeve_front = ImageDetailSerializer()
    tank_right_sleeve_front = ImageDetailSerializer()

    class Meta:
        model = models.TankTop_Front
        fields = ['id', 'name',
                  'tank_collar_front',
                  'tank_collar_inner_front',
                  'tank_top_front',
                  'tank_mid_front',
                  'tank_bottom_front',
                  'tank_left_sleeve_front',
                  'tank_right_sleeve_front',
                  ]


class BackViewTankTopDetailSerializer(serializers.ModelSerializer):
    tank_collar_back = ImageDetailSerializer()
    tank_top_back = ImageDetailSerializer()
    tank_mid_back = ImageDetailSerializer()
    tank_bottom_back = ImageDetailSerializer()
    tank_left_sleeve_back = ImageDetailSerializer()
    tank_right_sleeve_back = ImageDetailSerializer()

    class Meta:
        model = models.TankTop_Back
        fields = ['id', 'name',
                  'tank_collar_back',
                  'tank_top_back',
                  'tank_mid_back',
                  'tank_bottom_back',
                  'tank_left_sleeve_back',
                  'tank_right_sleeve_back',
                  ]


# class TankTopDetailSerializer(serializers.ModelSerializer):
#     front_view_tank_top = TankTopFrontSerializer()
#     back_view_tank_top = TankTopBackSerializer()
#
#     class Meta:
#         model = models.ProductDesign
#         fields = ['id', 'name',
#                   'front_view_tank_top',
#                   'back_view_tank_top',
#                   ]
#
#     def get_front_view(self, obj):
#         if obj.front_view_tank_top:
#             serializer = TankTopFrontSerializer(obj.front_view_tank_top)
#             return serializer.data
#         else:
#             return None
#
#     def get_back_view(self, obj):
#         if obj.front_view_tank_top:
#             serializer = TankTopBackSerializer(obj.front_view_tank_top)
#             return serializer.data
#         else:
#             return None
