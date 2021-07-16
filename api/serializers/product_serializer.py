from rest_framework import serializers
from constructor import models


class ImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = models.ImageField
        fields = ['id', 'name', 'image','x_point', 'y_point', 'width', 'height']

    def get_image(self, obj):
        return 'http://localhost:8000'+obj.image.url


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
        fields = ['id', 'name', 'collar_strip', 'collar_strip_side', 'bukkle', 'body', 'left_strip', 'right_strip',
                  'pocket']


class HatFrontDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_front = ImageDetailSerializer()
    hat_dot_right_front = ImageDetailSerializer()
    hat_upper_part_front = ImageDetailSerializer()
    hat_lower_part_front = ImageDetailSerializer()
    hat_top_button_front = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_front', 'hat_dot_right_front', 'hat_upper_part_front',
                  'hat_lower_part_front', 'hat_top_button_front']


class HatLeftDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_left = ImageDetailSerializer()
    hat_dot_right_left = ImageDetailSerializer()
    hat_upper_part_left = ImageDetailSerializer()
    hat_lower_part_left = ImageDetailSerializer()
    hat_top_button_left = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_left', 'hat_dot_right_left', 'hat_upper_part_left',
                  'hat_lower_part_left', 'hat_top_button_left']


class HatRightDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_right = ImageDetailSerializer()
    hat_dot_right_right = ImageDetailSerializer()
    hat_upper_part_right = ImageDetailSerializer()
    hat_lower_part_right = ImageDetailSerializer()
    hat_top_button_right = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_right', 'hat_dot_right_right', 'hat_upper_part_right',
                  'hat_lower_part_right', 'hat_top_button_right']


class HatBackDetailSerializer(serializers.ModelSerializer):
    hat_dot_left_back = ImageDetailSerializer()
    hat_dot_right_back = ImageDetailSerializer()
    hat_upper_part_back = ImageDetailSerializer()
    hat_lower_strip_back = ImageDetailSerializer()

    class Meta:
        model = models.HatFront
        fields = ['id', 'name', 'hat_dot_left_back', 'hat_dot_right_back', 'hat_upper_part_back',
                  'hat_lower_strip_back']


class HatDetailSerializer(serializers.ModelSerializer):
    front_view_hat = HatFrontDetailSerializer()
    back_view_hat = HatBackDetailSerializer()
    left_view_hat = HatLeftDetailSerializer()
    right_view_hat = HatRightDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_hat', 'back_view_hat', 'left_view_hat', 'right_view_hat']



class TowelFrontDetailSerializer(serializers.ModelSerializer):
    towel_front = ImageDetailSerializer()

    class Meta:
        model = models.TowelFront
        fields = ['id', 'name', 'towel_front']


class TowelBackDetailSerializer(serializers.ModelSerializer):
    towel_back = ImageDetailSerializer()

    class Meta:
        model = models.TowelBack
        fields = ['id', 'name', 'towel_back']


class TowelDetailSerializer(serializers.ModelSerializer):
    front_view_towel = TowelFrontDetailSerializer()
    back_view_towel = TowelBackDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_towel', 'back_view_towel']


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
    vest_top = ImageDetailSerializer()
    vest_mid = ImageDetailSerializer()
    vest_bottom = ImageDetailSerializer()
    vest_pocket_left = ImageDetailSerializer()
    vest_pocket_right = ImageDetailSerializer()
    vest_hem = ImageDetailSerializer()
    vest_left_sleeve = ImageDetailSerializer()
    vest_right_sleeve = ImageDetailSerializer()

    class Meta:
        model = models.VestFront
        fields = ['id', 'name', 'collar_vest', 'zip_vest', 'vest_top',
                  'vest_mid',  'vest_bottom', 'vest_pocket_right',
                  'vest_pocket_left', 'vest_hem', 'vest_left_sleeve', 'vest_right_sleeve']


class VestBackDetailSerializer(serializers.ModelSerializer):
    collar_vest_back = ImageDetailSerializer()
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
        fields = ['id', 'name', 'collar_vest_back', 'vest_top_back', 'vest_mid_back',
                  'vest_bottom_back', 'vest_pocket_left_back', 'vest_pocket_right_back', 'vest_hem_back',
                  'vest_left_sleeve_back', 'vest_right_sleeve_back']


class VestDetailSerializer(serializers.ModelSerializer):
    front_view_vest = VestFrontDetailSerializer()
    back_view_vest = VestBackDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_vest', 'back_view_vest']


class BagFrontDetailSerializer(serializers.ModelSerializer):
    bag_handle_front = ImageDetailSerializer()
    bag_full_front_body = ImageDetailSerializer()
    bag_top_front_body = ImageDetailSerializer()
    bag_mid_front_body = ImageDetailSerializer()
    bag_bottom_front_body = ImageDetailSerializer()

    class Meta:
        model = models.BagFront
        fields = ['id', 'name', 'bag_handle_front', 'bag_full_front_body', 'bag_top_front_body', 'bag_mid_front_body',
                  'bag_bottom_front_body']


class BagBackDetailSerializer(serializers.ModelSerializer):
    bag_handle_back = ImageDetailSerializer()
    bag_full_back_body = ImageDetailSerializer()
    bag_top_back_body = ImageDetailSerializer()
    bag_mid_back_body = ImageDetailSerializer()
    bag_bottom_back_body = ImageDetailSerializer()

    class Meta:
        model = models.BagBack
        fields = ['id', 'name', 'bag_handle_back', 'bag_full_back_body', 'bag_top_back_body', 'bag_mid_back_body',
                  'bag_bottom_back_body']


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
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'key' ,'designs']

    def get_designs(self, obj):
        qs = models.ProductDesign.objects.filter(category=obj)
        serializer = ProductDesignWithCategorySerializers(qs, many=True)
        return serializer.data


class ProductDesignWithCategorySerializers(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'key','display_image']

    def get_key(self, obj):
        print(obj.category.key)
        return obj.category.key


class CategoryDetailSerializer(serializers.ModelSerializer):
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'designs']

    def get_designs(self, obj):
        qs = models.ProductDesign.objects.filter(category=obj)
        serializer = ProductDesignWithCategorySerializers(qs, many=True)
        return serializer.data
