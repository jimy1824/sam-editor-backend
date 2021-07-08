from rest_framework import serializers
from constructor import models


class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageField
        fields = ['id', 'name', 'image', 'x_point', 'y_point', 'width', 'height']


class TowelSerializer(serializers.ModelSerializer):
    towel_front = ImageDetailSerializer()
    towel_back = ImageDetailSerializer()

    class Meta:
        model = models.Towel
        fields = ['id', 'name', 'towel_front', 'towel_back']


class ApronDetailSerializer(serializers.ModelSerializer):
    collar_strip = ImageDetailSerializer()
    collar_strip_side = ImageDetailSerializer()
    bukkle = ImageDetailSerializer()
    body = ImageDetailSerializer()
    left_strip = ImageDetailSerializer()
    right_strip = ImageDetailSerializer()
    pocket = ImageDetailSerializer()

    class Meta:
        model = models.Apron
        fields = ['id', 'name', 'collar_strip', 'collar_strip_side', 'bukkle', 'body', 'left_strip', 'right_strip', 'pocket']


class PantFrontDetailSerializer(serializers.ModelSerializer):
    pant_upper_waist_front = ImageDetailSerializer()
    pant_lower_waist_front = ImageDetailSerializer()
    pant_thai_left_front = ImageDetailSerializer()
    pant_thai_right_front = ImageDetailSerializer()
    pant_knees_left_front = ImageDetailSerializer()
    pant_knees_right_front = ImageDetailSerializer()
    pant_bottom_left_front = ImageDetailSerializer()
    pant_bottom_right_front = ImageDetailSerializer()
    pant_pocket_left_front = ImageDetailSerializer()
    pant_pocket_right_front = ImageDetailSerializer()

    class Meta:
        model = models.PantFront
        fields = ['id', 'name', 'pant_upper_waist_front', 'pant_lower_waist_front', 'pant_thai_left_front',
                  'pant_thai_right_front', 'pant_knees_left_front', 'pant_knees_right_front',
                  'pant_bottom_left_front',
                  'pant_bottom_right_front',
                  'pant_pocket_left_front',
                  'pant_pocket_right_front']



class VestFrontDetailSerializer(serializers.ModelSerializer):
    collar_vest = ImageDetailSerializer()
    zip_vest = ImageDetailSerializer()
    vest_top_full = ImageDetailSerializer()
    vest_top_left = ImageDetailSerializer()
    vest_top_right = ImageDetailSerializer()
    vest_mid_left = ImageDetailSerializer()
    vest_mid_right = ImageDetailSerializer()
    vest_bottom_left = ImageDetailSerializer()
    vest_bottom_right = ImageDetailSerializer()
    vest_pocket_left = ImageDetailSerializer()
    vest_pocket_right = ImageDetailSerializer()
    vest_hem = ImageDetailSerializer()
    vest_left_sleeve = ImageDetailSerializer()
    vest_right_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.VestFront
        fields = ['id', 'name', 'collar_vest', 'zip_vest', 'vest_top_full', 'vest_top_left',
                  'vest_top_right', 'vest_mid_left', 'vest_mid_right', 'vest_bottom_left', 'vest_bottom_right',
                  'vest_pocket_left', 'vest_hem', 'vest_left_sleeve', 'vest_right_sleeve']


class VestBackDetailSerializer(serializers.ModelSerializer):
    collar_vest_back = ImageDetailSerializer()
    vest_full_back = ImageDetailSerializer()
    vest_top_back = ImageDetailSerializer()
    vest_mid_back = ImageDetailSerializer()
    vest_bottom_back = ImageDetailSerializer()
    vest_pocket_left_back = ImageDetailSerializer()
    vest_pocket_right_back = ImageDetailSerializer()
    vest_hem_back = ImageDetailSerializer()
    vest_left_sleeve_back = ImageDetailSerializer()
    vest_right_sleeve_back = ImageDetailSerializer()

    class Meta:
        model = models.VestBack
        fields = ['id', 'name', 'collar_vest_back', 'vest_full_back', 'vest_top_back', 'vest_mid_back',
                  'vest_bottom_back', 'vest_pocket_left_back', 'vest_pocket_right_back', 'vest_hem_back', 'vest_bottom_right',
                  'vest_left_sleeve_back', 'vest_right_sleeve_back']



class BodyDetailSerializer(serializers.ModelSerializer):
    body_view = ImageDetailSerializer()
    body_first_section = ImageDetailSerializer()
    body_second_section = ImageDetailSerializer()
    body_third_section = ImageDetailSerializer()
    collar = ImageDetailSerializer()
    hem = ImageDetailSerializer()
    right_sleeve = ImageDetailSerializer()
    left_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.Body
        fields = ['id', 'name', 'body_view', 'body_first_section', 'body_second_section', 'body_third_section',
                  'collar', 'hem', 'right_sleeve', 'left_sleeve']


class LeftViewSerializer(serializers.ModelSerializer):
    left_v_body_view = ImageDetailSerializer()
    left_v_upper_part = ImageDetailSerializer()
    left_v_lower_part = ImageDetailSerializer()
    left_v_left_s_upper = ImageDetailSerializer()
    left_v_left_s_lower = ImageDetailSerializer()
    left_v_right_s_upper = ImageDetailSerializer()
    left_v_right_s_lower = ImageDetailSerializer()

    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'left_v_body_view', 'left_v_upper_part', 'left_v_lower_part', 'left_v_left_s_upper',
                  'left_v_left_s_lower', 'left_v_right_s_upper', 'left_v_right_s_lower']


class RightViewSerializer(serializers.ModelSerializer):
    right_v_body_view = ImageDetailSerializer()
    right_v_upper_part = ImageDetailSerializer()
    right_v_lower_part = ImageDetailSerializer()
    right_v_left_s_upper = ImageDetailSerializer()
    right_v_left_s_lower = ImageDetailSerializer()
    right_v_right_s_upper = ImageDetailSerializer()
    right_v_right_s_lower = ImageDetailSerializer()

    class Meta:
        model = models.RightView
        fields = ['id', 'name', 'right_v_body_view', 'right_v_upper_part', 'right_v_lower_part', 'right_v_left_s_upper',
                  'right_v_left_s_lower', 'right_v_right_s_upper', 'right_v_right_s_lower']


class BackViewSerializer(serializers.ModelSerializer):
    back_first_part = ImageDetailSerializer()
    back_second_part = ImageDetailSerializer()
    back_third_part = ImageDetailSerializer()
    back_left_sleeve = ImageDetailSerializer()
    back_right_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'back_first_part', 'back_second_part', 'back_third_part', 'back_left_sleeve',
                  'back_right_sleeve']


class ProductDetailSerializer(serializers.ModelSerializer):
    front_view = BodyDetailSerializer()
    left_view = LeftViewSerializer()
    right_view = RightViewSerializer()
    back_view = BackViewSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view', 'left_view', 'right_view', 'back_view']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class CategoryListSerializer(serializers.ModelSerializer):
    # designs = ProductListSerializer(source='productdesign_set', many=True)
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']

    def get_designs(self, object):
        if object.key == "towel":
            serializers = TowelSerializer(models.Towel.objects.all(), many=True)
            return serializers.data

        if object.key == "apron":
            serializers = ApronDetailSerializer(models.Apron.objects.all(), many=True)
            return serializers.data