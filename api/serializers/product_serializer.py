from rest_framework import serializers
from constructor import models
from .shirt import (FrontViewShirtDetailSerializer, BackViewShirtSerializer, LeftViewShirtSerializer,
                    RightViewShirtSerializer)

from .apron import FrontViewApronDetailSerializer
from .bag import FrontViewBagDetailSerializer, BackViewBagDetailSerializer
from .base_ball_jacket import (FrontViewBaseBallJacketDetailSerializer, BackViewBaseBallJacketDetailSerializer,
                               LeftViewBaseBallJacketDetailSerializer, RightViewBaseBallJacketDetailSerializer)
from .base_ball_shirt import (FrontViewBaseBallShirtDetailSerializer, BackViewBaseBallShirtDetailSerializer,
                              LeftViewBaseBallShirtDetailSerializer, RightViewBaseBallShirtDetailSerializer)

from .bomber_jacket import (FrontViewBomberJacketDetailSerializer, BackViewBomberJacketDetailSerializer,
                            LeftViewBomberJacketDetailSerializer, RightViewBomberJacketDetailSerializer)

from .coach_jacket import (FrontViewCoachJacketDetailSerializer, BackViewCoachJacketDetailSerializer,
                           LeftViewCoachJacketDetailSerializer, RightViewCoachJacketDetailSerializer)

from .hat import (FrontViewHatDetailSerializer, BackViewHatDetailSerializer, LeftViewHatDetailSerializer,
                  RightViewHatDetailSerializer)

from .hoodie import (FrontViewHoodieDetailSerializer, BackViewHoodieDetailSerializer, RightViewHoodieDetailSerializer,
                     LeftViewHoodieDetailSerializer)

from .pant import (FrontViewPantDetailSerializer, BackViewPantDetailSerializer)
from .tank_top import (FrontViewTankTopDetailSerializer, BackViewTankTopDetailSerializer)
from .towel import (FrontViewTowelDetailSerializer, BackViewTowelDetailSerializer)
from .vest import (FrontViewVestDetailSerializer, BackViewVestDetailSerializer)


class CategoryListSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'key', 'selected']

    def get_selected(self, obj):
        return False

    # def get_designs(self, obj):
    #     qs = models.ProductDesign.objects.filter(category=obj)
    #     serializer = ProductDesignWithCategorySerializers(qs, many=True)
    #     return serializer.data


class ColorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ['id', 'name', 'color_code']


class FabricDetailSerializer(serializers.ModelSerializer):
    colors = ColorDetailSerializer(many=True)
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Fabric
        fields = ['id', 'name', 'selected', 'colors', 'short_description']

    def get_selected(self, obj):
        return False


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class ProductDesignWithCategorySerializers(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'key', 'category_id', 'display_image', 'selected']

    def get_key(self, obj):
        return obj.category.key

    def get_category_id(self, obj):
        return obj.category.id

    def get_selected(self, obj):
        return False


class CategoryDetailSerializer(serializers.ModelSerializer):
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']

    def get_designs(self, obj):
        qs = models.ProductDesign.objects.filter(category=obj)
        serializer = ProductDesignWithCategorySerializers(qs, many=True)
        return serializer.data


class ProductDetailSerializer(serializers.ModelSerializer):
    fabrics = FabricDetailSerializer(many=True)
    front_view = serializers.SerializerMethodField()

    # back_view = serializers.SerializerMethodField()

    # front_view = BodyDetailSerializer()
    # left_view = LeftViewSerializer()
    # right_view = RightViewSerializer()
    # back_view = BackViewSerializer()

    class Meta:
        model = models.ProductDesign
        # fields = ['id', 'name', 'fabrics', 'front_view', 'left_view', 'right_view', 'back_view']
        fields = ['id', 'name', 'fabrics', 'front_view']

    def get_front_view(self, obj):
        if obj.category.key == 'polo-shirt':
            serializer = FrontViewShirtDetailSerializer(obj.front_view)
            return serializer.data
        if obj.category.key == 'shirt':
            serializer = FrontViewShirtDetailSerializer(obj.front_view)
            return serializer.data
        if obj.category.key == 'apron':
            serializer = FrontViewApronDetailSerializer(obj.front_view_apron)
            return serializer.data
        if obj.category.key == 'bag':
            serializer = FrontViewBagDetailSerializer(obj.front_view_bag)
            return serializer.data
        if obj.category.key == 'base-ball-jacket':
            serializer = FrontViewBaseBallJacketDetailSerializer(obj.front_view_base_b_jacket)
            return serializer.data
        if obj.category.key == 'base-ball-shirt':
            serializer = FrontViewBaseBallShirtDetailSerializer(obj.front_view_base_b_shirt)
            return serializer.data
        if obj.category.key == 'bomber-jacket':
            serializer = FrontViewBomberJacketDetailSerializer(obj.front_view_bomber_jac)
            return serializer.data
        if obj.category.key == 'hat':
            serializer = FrontViewHatDetailSerializer(obj.front_view_hat)
            return serializer.data
        if obj.category.key == 'hoodie':
            serializer = FrontViewHoodieDetailSerializer(obj.front_view_hoodie)
            return serializer.data
        if obj.category.key == 'pants':
            serializer = FrontViewPantDetailSerializer(obj.front_view_pant)
            return serializer.data
        if obj.category.key == 'tank-top':
            serializer = FrontViewTankTopDetailSerializer(obj.front_view_tank_top)
            return serializer.data
        if obj.category.key == 'towel':
            serializer = FrontViewTowelDetailSerializer(obj.front_view_towel)
            return serializer.data
        if obj.category.key == 'vest':
            serializer = FrontViewVestDetailSerializer(obj.front_view_vest)
            return serializer.data

        return None



        #


        #

        #

        #

        #
        # if product_design.category.key == 'coach-jacket':
        #     serializer = product_serializer.CoachJacDetailSerializer(product_design)
        #     return Response(serializer.data)
        #

        #

        #

        #


