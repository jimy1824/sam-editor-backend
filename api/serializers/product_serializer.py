from rest_framework import serializers
from constructor import models


class ImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    type=serializers.SerializerMethodField()

    class Meta:
        model = models.ImageField
        fields = ['id', 'name', 'image', 'x_point', 'y_point', 'width', 'height','type']

    def get_image(self, obj):
        # return 'http://localhost:8000' + obj.image.url
        return 'http://44.192.67.250' + obj.image.url

    def get_type(self, obj):
        if self.context.get('type'):
            return self.context.get('type')
        return None



class ApronFrontDetailSerializer(serializers.ModelSerializer):
    collar_strip = ImageDetailSerializer()
    collar_strip_side = ImageDetailSerializer()
    bukkle = ImageDetailSerializer()
    appren_body = serializers.SerializerMethodField()
    left_strip = ImageDetailSerializer()
    right_strip = ImageDetailSerializer()
    pocket = ImageDetailSerializer()

    class Meta:
        model = models.Apron
        fields = ['id', 'name', 'collar_strip', 'collar_strip_side', 'bukkle', 'appren_body', 'left_strip', 'right_strip',
                  'pocket']

    def get_appren_body(self, obj):
        serializer = ImageDetailSerializer(obj.body)
        return serializer.data


class ApronDetailSerializer(serializers.ModelSerializer):
    front_view_apron = ApronFrontDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_apron']


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


class PantBackDetailSerializer(serializers.ModelSerializer):
    pant_upper_waist_back = ImageDetailSerializer()
    pant_lower_waist_back = ImageDetailSerializer()
    pant_thai_left_back = ImageDetailSerializer()
    pant_thai_right_back = ImageDetailSerializer()
    pant_knees_left_back = ImageDetailSerializer()
    pant_knees_right_back = ImageDetailSerializer()
    pant_bottom_left_back = ImageDetailSerializer()
    pant_bottom_right_back = ImageDetailSerializer()
    pant_pocket_left_back = ImageDetailSerializer()
    pant_pocket_right_back = ImageDetailSerializer()

    class Meta:
        model = models.PantBack
        fields = ['id', 'name', 'pant_upper_waist_back', 'pant_lower_waist_back', 'pant_thai_left_back',
                  'pant_thai_right_back', 'pant_knees_left_back', 'pant_knees_right_back',
                  'pant_bottom_left_back',
                  'pant_bottom_right_back',
                  'pant_pocket_left_back',
                  'pant_pocket_right_back']


class PantDetailSerializer(serializers.ModelSerializer):
    front_view_pant = PantFrontDetailSerializer()
    back_view_pant = PantBackDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_pant', 'back_view_pant']


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
                  'vest_mid', 'vest_bottom', 'vest_pocket_right',
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
    right_sleeve = serializers.SerializerMethodField()
    left_sleeve = serializers.SerializerMethodField()

    class Meta:
        model = models.Body
        fields = ['id', 'name', 'body_view', 'body_first_section', 'body_second_section', 'body_third_section',
                  'collar', 'hem', 'right_sleeve', 'left_sleeve']

    def get_right_sleeve(self, obj):
        serializer =  ImageDetailSerializer(obj.right_sleeve,context={'type':'sleeve'})
        return serializer.data

    def get_left_sleeve(self, obj):
        serializer =  ImageDetailSerializer(obj.left_sleeve,context={'type':'sleeve'})
        return serializer.data

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
    back_left_sleeve = serializers.SerializerMethodField()
    back_right_sleeve = serializers.SerializerMethodField()

    class Meta:
        model = models.LeftView
        fields = ['id', 'name', 'back_first_part', 'back_second_part', 'back_third_part', 'back_left_sleeve',
                  'back_right_sleeve']

    def get_back_left_sleeve(self, obj):
        serializer =  ImageDetailSerializer(obj.back_left_sleeve,context={'type':'sleeve'})
        return serializer.data

    def get_back_right_sleeve(self, obj):
        serializer =  ImageDetailSerializer(obj.back_right_sleeve,context={'type':'sleeve'})
        return serializer.data

class ProductDetailSerializer(serializers.ModelSerializer):
    front_view = BodyDetailSerializer()
    left_view = LeftViewSerializer()
    right_view = RightViewSerializer()
    back_view = BackViewSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view', 'left_view', 'right_view', 'back_view']


class BaseBJacketFrontViewSerializer(serializers.ModelSerializer):
    base_b_jac_front_body = ImageDetailSerializer()
    base_b_jac_front_collar = ImageDetailSerializer()
    base_b_jac_front_collar_inner = ImageDetailSerializer()
    base_b_jac_front_hem = ImageDetailSerializer()
    base_b_jac_front_hem_strips = ImageDetailSerializer()
    base_b_jac_front_hem_mid = ImageDetailSerializer()
    base_b_jac_front_button_body = ImageDetailSerializer()
    base_b_jac_front_button_hem = ImageDetailSerializer()
    base_b_jac_left_pocket_front = ImageDetailSerializer()
    base_b_jac_right_pocket_front = ImageDetailSerializer()
    base_b_jac_left_sleeve_front = ImageDetailSerializer()
    base_b_jac_left_cuff_front = ImageDetailSerializer()
    base_b_jac_left_cuff_front_strips = ImageDetailSerializer()
    base_b_jac_right_sleeve_front = ImageDetailSerializer()
    base_b_jac_right_cuff_front = ImageDetailSerializer()
    base_b_jac_right_cuff_front_strips = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Front
        fields = ['id', 'name', 'base_b_jac_front_body', 'base_b_jac_front_collar',
                  'base_b_jac_front_collar_inner', 'base_b_jac_front_hem', 'base_b_jac_front_hem_strips',
                  'base_b_jac_front_hem_mid', 'base_b_jac_front_button_body', 'base_b_jac_front_button_hem',
                  'base_b_jac_left_pocket_front', 'base_b_jac_right_pocket_front', 'base_b_jac_left_sleeve_front',
                  'base_b_jac_left_cuff_front', 'base_b_jac_left_cuff_front_strips', 'base_b_jac_right_sleeve_front',
                  'base_b_jac_right_cuff_front', 'base_b_jac_right_cuff_front_strips'
                  ]


class BaseBJacketBackViewSerializer(serializers.ModelSerializer):
    base_b_jac_collar_back = ImageDetailSerializer()
    base_b_jac_collar_strips_back = ImageDetailSerializer()
    base_b_jac_body_back = ImageDetailSerializer()
    base_b_jac_hem_back = ImageDetailSerializer()
    base_b_jac_hem_strips_back = ImageDetailSerializer()
    base_b_jac_left_sleeve_back = ImageDetailSerializer()
    base_b_jac_left_cuff_back = ImageDetailSerializer()
    base_b_jac_left_cuff_strip_back = ImageDetailSerializer()
    base_b_jac_right_sleeve_back = ImageDetailSerializer()
    base_b_jac_right_cuff_back = ImageDetailSerializer()
    base_b_jac_right_cuff_strip_back = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Back

        fields = ['id', 'name',
                  'base_b_jac_collar_back',
                  'base_b_jac_collar_strips_back',
                  'base_b_jac_body_back',
                  'base_b_jac_hem_back',
                  'base_b_jac_hem_strips_back',
                  'base_b_jac_left_sleeve_back',
                  'base_b_jac_left_cuff_back',
                  'base_b_jac_left_cuff_strip_back',
                  'base_b_jac_right_sleeve_back',
                  'base_b_jac_right_cuff_back',
                  'base_b_jac_right_cuff_strip_back',
                  ]


class BaseBJacketLeftViewSerializer(serializers.ModelSerializer):
    base_b_jac_mid_body_left = ImageDetailSerializer()
    base_b_jac_mid_cuff_left = ImageDetailSerializer()
    base_b_jac_mid_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_left_body_left = ImageDetailSerializer()
    base_b_jac_left_cuff_left = ImageDetailSerializer()
    base_b_jac_left_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_right_body_left = ImageDetailSerializer()
    base_b_jac_right_cuff_left = ImageDetailSerializer()
    base_b_jac_right_cuff_strips_left = ImageDetailSerializer()
    base_b_jac_bottom_body_left = ImageDetailSerializer()
    base_b_jac_bottom_cuff_left = ImageDetailSerializer()
    base_b_jac_bottom_cuff_strips_left = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Left

        fields = ['id', 'name',
                  'base_b_jac_mid_body_left',
                  'base_b_jac_mid_cuff_left',
                  'base_b_jac_mid_cuff_strips_left',
                  'base_b_jac_left_body_left',
                  'base_b_jac_left_cuff_left',
                  'base_b_jac_left_cuff_strips_left',
                  'base_b_jac_right_body_left',
                  'base_b_jac_right_cuff_left',
                  'base_b_jac_right_cuff_strips_left',
                  'base_b_jac_bottom_body_left',
                  'base_b_jac_bottom_cuff_left',
                  'base_b_jac_bottom_cuff_strips_left',
                  ]


class BaseBJacketRightViewSerializer(serializers.ModelSerializer):
    base_b_jac_mid_body_right = ImageDetailSerializer()
    base_b_jac_mid_cuff_right = ImageDetailSerializer()
    base_b_jac_mid_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_left_body_right = ImageDetailSerializer()
    base_b_jac_left_cuff_right = ImageDetailSerializer()
    base_b_jac_left_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_right_body_right = ImageDetailSerializer()
    base_b_jac_right_cuff_right = ImageDetailSerializer()
    base_b_jac_right_cuff_strips_right = ImageDetailSerializer()
    base_b_jac_bottom_body_right = ImageDetailSerializer()
    base_b_jac_bottom_cuff_right = ImageDetailSerializer()
    base_b_jac_bottom_cuff_strips_right = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallJacket_Right
        fields = ['id', 'name',
                  'base_b_jac_mid_body_right',
                  'base_b_jac_mid_cuff_right',
                  'base_b_jac_mid_cuff_strips_right',
                  'base_b_jac_left_body_right',
                  'base_b_jac_left_cuff_right',
                  'base_b_jac_left_cuff_strips_right',
                  'base_b_jac_right_body_right',
                  'base_b_jac_right_cuff_right',
                  'base_b_jac_right_cuff_strips_right',
                  'base_b_jac_bottom_body_right',
                  'base_b_jac_bottom_cuff_right',
                  'base_b_jac_bottom_cuff_strips_right',
                  ]


class BaseBJacDetailSerializer(serializers.ModelSerializer):
    front_view_base_b_jacket = BaseBJacketFrontViewSerializer()
    back_view_base_b_jacket = BaseBJacketBackViewSerializer()
    left_view_base_b_jacket = BaseBJacketLeftViewSerializer()
    right_view_base_b_jacket = BaseBJacketRightViewSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_base_b_jacket', 'back_view_base_b_jacket', 'left_view_base_b_jacket',
                  'right_view_base_b_jacket'
                  ]


class CoachJacFrontSerializer(serializers.ModelSerializer):
    coach_jac_body_front = ImageDetailSerializer()
    coach_jac_collar_front = ImageDetailSerializer()
    coach_jac_collar_inner_front = ImageDetailSerializer()
    coach_jac_button_front = ImageDetailSerializer()
    coach_jac_left_pocket_front = ImageDetailSerializer()
    coach_jac_right_pocket_front = ImageDetailSerializer()
    coach_jac_hem_front = ImageDetailSerializer()
    coach_jac_left_sleeve_front = ImageDetailSerializer()
    coach_jac_right_sleeve_front = ImageDetailSerializer()
    coach_jac_left_cuff_front = ImageDetailSerializer()
    coach_jac_right_cuff_front = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Front
        fields = ['id', 'name',
                  'coach_jac_body_front',
                  'coach_jac_collar_front',
                  'coach_jac_collar_inner_front',
                  'coach_jac_button_front',
                  'coach_jac_left_pocket_front',
                  'coach_jac_right_pocket_front',
                  'coach_jac_hem_front',
                  'coach_jac_left_sleeve_front',
                  'coach_jac_right_sleeve_front',
                  'coach_jac_left_cuff_front',
                  'coach_jac_right_cuff_front',
                  ]


class CoachJacBackSerializer(serializers.ModelSerializer):
    coach_jac_body_back = ImageDetailSerializer()
    coach_jac_collar_back = ImageDetailSerializer()
    coach_jac_left_sleeve_back = ImageDetailSerializer()
    coach_jac_right_sleeve_back = ImageDetailSerializer()
    coach_jac_hem_back = ImageDetailSerializer()
    coach_jac_left_cuff_back = ImageDetailSerializer()
    coach_jac_right_cuff_back = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Back
        fields = ['id', 'name',
                  'coach_jac_body_back',
                  'coach_jac_collar_back',
                  'coach_jac_left_sleeve_back',
                  'coach_jac_right_sleeve_back',
                  'coach_jac_hem_back',
                  'coach_jac_left_cuff_back',
                  'coach_jac_right_cuff_back',
                  ]


class CoachJacLeftSerializer(serializers.ModelSerializer):
    coach_jac_mid_body_left = ImageDetailSerializer()
    coach_jac_left_body_left = ImageDetailSerializer()
    coach_jac_right_body_left = ImageDetailSerializer()
    coach_jac_bottom_body_left = ImageDetailSerializer()
    coach_jac_mid_cuff_left = ImageDetailSerializer()
    coach_jac_left_cuff_left = ImageDetailSerializer()
    coach_jac_right_cuff_left = ImageDetailSerializer()
    coach_jac_bottom_cuff_left = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Left
        fields = ['id', 'name',
                  'coach_jac_mid_body_left',
                  'coach_jac_left_body_left',
                  'coach_jac_right_body_left',
                  'coach_jac_bottom_body_left',
                  'coach_jac_mid_cuff_left',
                  'coach_jac_left_cuff_left',
                  'coach_jac_right_cuff_left',
                  'coach_jac_bottom_cuff_left',
                  ]


class CoachJacRightSerializer(serializers.ModelSerializer):
    coach_jac_mid_body_right = ImageDetailSerializer()
    coach_jac_left_body_right = ImageDetailSerializer()
    coach_jac_right_body_right = ImageDetailSerializer()
    coach_jac_bottom_body_right = ImageDetailSerializer()
    coach_jac_mid_cuff_right = ImageDetailSerializer()
    coach_jac_left_cuff_right = ImageDetailSerializer()
    coach_jac_right_cuff_right = ImageDetailSerializer()
    coach_jac_bottom_cuff_right = ImageDetailSerializer()

    class Meta:
        model = models.CoachJacket_Right
        fields = ['id', 'name',
                  'coach_jac_mid_body_right',
                  'coach_jac_left_body_right',
                  'coach_jac_right_body_right',
                  'coach_jac_bottom_body_right',
                  'coach_jac_mid_cuff_right',
                  'coach_jac_left_cuff_right',
                  'coach_jac_right_cuff_right',
                  'coach_jac_bottom_cuff_right',
                  ]


class CoachJacDetailSerializer(serializers.ModelSerializer):
    front_view_coach_jac = CoachJacFrontSerializer()
    back_view_base_coach_jac = CoachJacBackSerializer()
    left_view_coach_jac = CoachJacLeftSerializer()
    right_view_coach_jac = CoachJacRightSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'front_view_coach_jac', 'back_view_base_coach_jac', 'left_view_coach_jac',
                  'right_view_coach_jac'
                  ]


class HoodieFrontSerializer(serializers.ModelSerializer):
    cap_left = ImageDetailSerializer()
    cap_right = ImageDetailSerializer()
    cap_inner_mid = ImageDetailSerializer()
    cap_inner_left = ImageDetailSerializer()
    cap_inner_right = ImageDetailSerializer()
    cap_inner_bottom = ImageDetailSerializer()
    hood_left_strip = ImageDetailSerializer()
    hood_right_strip = ImageDetailSerializer()
    zip = ImageDetailSerializer()
    hood_top = ImageDetailSerializer()
    hood_top_left = ImageDetailSerializer()
    hood_top_right = ImageDetailSerializer()
    hood_mid = ImageDetailSerializer()
    hood_mid_left = ImageDetailSerializer()
    hood_mid_right = ImageDetailSerializer()
    hood_bottom = ImageDetailSerializer()
    hood_bottom_left = ImageDetailSerializer()
    hood_bottom_right = ImageDetailSerializer()
    hood_hem_left = ImageDetailSerializer()
    hood_hem_right = ImageDetailSerializer()
    hood_left_sleeve_full = ImageDetailSerializer()
    hood_left_sleeve_top = ImageDetailSerializer()
    hood_left_sleeve_mid = ImageDetailSerializer()
    hood_left_sleeve_bottom = ImageDetailSerializer()
    hood_left_sleeve_cuff = ImageDetailSerializer()
    hood_left_sleeve_cuff_strips = ImageDetailSerializer()
    hood_right_sleeve_full = ImageDetailSerializer()
    hood_right_sleeve_top = ImageDetailSerializer()
    hood_right_sleeve_mid = ImageDetailSerializer()
    hood_right_sleeve_bottom = ImageDetailSerializer()
    hood_right_sleeve_cuff = ImageDetailSerializer()
    hood_right_sleeve_cuff_strips = ImageDetailSerializer()

    class Meta:
        model = models.HoodieFront
        fields = ['id', 'name',
                  'cap_left',
                  'cap_right',
                  'cap_inner_mid',
                  'cap_inner_left',
                  'cap_inner_right',
                  'cap_inner_bottom',
                  'hood_left_strip',
                  'hood_right_strip',
                  'zip',
                  'hood_top',
                  'hood_top_left',
                  'hood_top_right',
                  'hood_mid',
                  'hood_mid_left',
                  'hood_mid_right',
                  'hood_bottom',
                  'hood_bottom_left',
                  'hood_bottom_right',
                  'hood_hem_left',
                  'hood_hem_right',
                  'hood_left_sleeve_full',
                  'hood_left_sleeve_top',
                  'hood_left_sleeve_mid',
                  'hood_left_sleeve_bottom',
                  'hood_left_sleeve_cuff',
                  'hood_left_sleeve_cuff_strips',
                  'hood_right_sleeve_full',
                  'hood_right_sleeve_top',
                  'hood_right_sleeve_mid',
                  'hood_right_sleeve_bottom',
                  'hood_right_sleeve_cuff',
                  'hood_right_sleeve_cuff_strips',
                  ]


class HoodieBackSerializer(serializers.ModelSerializer):
    cap_left_back = ImageDetailSerializer()
    cap_right_back = ImageDetailSerializer()
    hood_top_back = ImageDetailSerializer()
    hood_top_left_back = ImageDetailSerializer()
    hood_top_right_back = ImageDetailSerializer()
    hood_mid_back = ImageDetailSerializer()
    hood_mid_left_back = ImageDetailSerializer()
    hood_mid_right_back = ImageDetailSerializer()
    hood_bottom_back = ImageDetailSerializer()
    hood_bottom_left_back = ImageDetailSerializer()
    hood_bottom_right_back = ImageDetailSerializer()
    hood_hem_back = ImageDetailSerializer()
    hood_left_sleeve_full_back = ImageDetailSerializer()
    hood_left_sleeve_top_back = ImageDetailSerializer()
    hood_left_sleeve_mid_back = ImageDetailSerializer()
    hood_left_sleeve_bottom_back = ImageDetailSerializer()
    hood_left_sleeve_cuff_back = ImageDetailSerializer()
    hood_left_sleeve_cuff_strips_back = ImageDetailSerializer()
    hood_right_sleeve_full_back = ImageDetailSerializer()
    hood_right_sleeve_top_back = ImageDetailSerializer()
    hood_right_sleeve_mid_back = ImageDetailSerializer()
    hood_right_sleeve_bottom_back = ImageDetailSerializer()
    hood_right_sleeve_cuff_back = ImageDetailSerializer()
    hood_right_sleeve_cuff_strips_back = ImageDetailSerializer()

    class Meta:
        model = models.HoodieBack
        fields = ['id', 'name',
                  'cap_left_back',
                  'cap_right_back',
                  'hood_top_back',
                  'hood_top_left_back',
                  'hood_top_right_back',
                  'hood_mid_back',
                  'hood_mid_left_back',
                  'hood_mid_right_back',
                  'hood_bottom_back',
                  'hood_bottom_left_back',
                  'hood_bottom_right_back',
                  'hood_hem_back',
                  'hood_left_sleeve_full_back',
                  'hood_left_sleeve_top_back',
                  'hood_left_sleeve_mid_back',
                  'hood_left_sleeve_bottom_back',
                  'hood_left_sleeve_cuff_back',
                  'hood_left_sleeve_cuff_strips_back',
                  'hood_right_sleeve_full_back',
                  'hood_right_sleeve_top_back',
                  'hood_right_sleeve_mid_back',
                  'hood_right_sleeve_bottom_back',
                  'hood_right_sleeve_cuff_back',
                  'hood_right_sleeve_cuff_strips_back',
                  ]


class HoodieLeftSerializer(serializers.ModelSerializer):
    mid_full_body_hoodie_left = ImageDetailSerializer()
    mid_top_hoodie_left = ImageDetailSerializer()
    mid_mid_hoodie_left = ImageDetailSerializer()
    mid_bottom_hoodie_left = ImageDetailSerializer()
    mid_cuff_hoodie_left = ImageDetailSerializer()
    mid_cuff_strips_hoodie_left = ImageDetailSerializer()
    left_full_body_hoodie_left = ImageDetailSerializer()
    left_top_hoodie_left = ImageDetailSerializer()
    left_mid_hoodie_left = ImageDetailSerializer()
    left_bottom_hoodie_left = ImageDetailSerializer()
    left_cuff_hoodie_left = ImageDetailSerializer()
    left_cuff_strips_hoodie_left = ImageDetailSerializer()
    right_full_body_hoodie_left = ImageDetailSerializer()
    right_top_hoodie_left = ImageDetailSerializer()
    right_mid_hoodie_left = ImageDetailSerializer()
    right_bottom_hoodie_left = ImageDetailSerializer()
    right_cuff_hoodie_left = ImageDetailSerializer()
    right_cuff_strips_hoodie_left = ImageDetailSerializer()
    bottom_full_body_hoodie_left = ImageDetailSerializer()
    bottom_top_hoodie_left = ImageDetailSerializer()
    bottom_mid_hoodie_left = ImageDetailSerializer()
    bottom_bottom_hoodie_left = ImageDetailSerializer()
    bottom_cuff_hoodie_left = ImageDetailSerializer()
    bottom_cuff_strips_hoodie_left = ImageDetailSerializer()

    class Meta:
        model = models.HoodieLeft
        fields = ['id', 'name',
                  'mid_full_body_hoodie_left',
                  'mid_top_hoodie_left',
                  'mid_mid_hoodie_left',
                  'mid_bottom_hoodie_left',
                  'mid_cuff_hoodie_left',
                  'mid_cuff_strips_hoodie_left',
                  'left_full_body_hoodie_left',
                  'left_top_hoodie_left',
                  'left_mid_hoodie_left',
                  'left_bottom_hoodie_left',
                  'left_cuff_hoodie_left',
                  'left_cuff_strips_hoodie_left',
                  'right_full_body_hoodie_left',
                  'right_top_hoodie_left',
                  'right_mid_hoodie_left',
                  'right_bottom_hoodie_left',
                  'right_cuff_hoodie_left',
                  'right_cuff_strips_hoodie_left',
                  'bottom_full_body_hoodie_left',
                  'bottom_top_hoodie_left',
                  'bottom_mid_hoodie_left',
                  'bottom_bottom_hoodie_left',
                  'bottom_cuff_hoodie_left',
                  'bottom_cuff_strips_hoodie_left',
                  ]


class HoodieRightSerializer(serializers.ModelSerializer):
    mid_full_body_hoodie_right = ImageDetailSerializer()
    mid_top_hoodie_right = ImageDetailSerializer()
    mid_mid_hoodie_right = ImageDetailSerializer()
    mid_bottom_hoodie_right = ImageDetailSerializer()
    mid_cuff_hoodie_right = ImageDetailSerializer()
    mid_cuff_strips_hoodie_right = ImageDetailSerializer()
    left_full_body_hoodie_right = ImageDetailSerializer()
    left_top_hoodie_right = ImageDetailSerializer()
    left_mid_hoodie_right = ImageDetailSerializer()
    left_bottom_hoodie_right = ImageDetailSerializer()
    left_cuff_hoodie_right = ImageDetailSerializer()
    left_cuff_strips_hoodie_right = ImageDetailSerializer()
    right_full_body_hoodie_right = ImageDetailSerializer()
    right_top_hoodie_right = ImageDetailSerializer()
    right_mid_hoodie_right = ImageDetailSerializer()
    right_bottom_hoodie_right = ImageDetailSerializer()
    right_cuff_hoodie_right = ImageDetailSerializer()
    right_cuff_strips_hoodie_right = ImageDetailSerializer()
    bottom_full_body_hoodie_right = ImageDetailSerializer()
    bottom_top_hoodie_right = ImageDetailSerializer()
    bottom_mid_hoodie_right = ImageDetailSerializer()
    bottom_bottom_hoodie_right = ImageDetailSerializer()
    bottom_cuff_hoodie_right = ImageDetailSerializer()
    bottom_cuff_strips_hoodie_right = ImageDetailSerializer()

    class Meta:
        model = models.HoodieRight
        fields = ['id', 'name',
                  'mid_full_body_hoodie_right',
                  'mid_top_hoodie_right',
                  'mid_mid_hoodie_right',
                  'mid_bottom_hoodie_right',
                  'mid_cuff_hoodie_right',
                  'mid_cuff_strips_hoodie_right',
                  'left_full_body_hoodie_right',
                  'left_top_hoodie_right',
                  'left_mid_hoodie_right',
                  'left_bottom_hoodie_right',
                  'left_cuff_hoodie_right',
                  'left_cuff_strips_hoodie_right',
                  'right_full_body_hoodie_right',
                  'right_top_hoodie_right',
                  'right_mid_hoodie_right',
                  'right_bottom_hoodie_right',
                  'right_cuff_hoodie_right',
                  'right_cuff_strips_hoodie_right',
                  'bottom_full_body_hoodie_right',
                  'bottom_top_hoodie_right',
                  'bottom_mid_hoodie_right',
                  'bottom_bottom_hoodie_right',
                  'bottom_cuff_hoodie_right',
                  'bottom_cuff_strips_hoodie_right',
                  ]


class HoodieDetailSerializer(serializers.ModelSerializer):
    front_view_hoodie = HoodieFrontSerializer()
    back_view_hoodie = HoodieBackSerializer()
    left_view_hoodie = HoodieLeftSerializer()
    right_view_hoodie = HoodieRightSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name',
                  'front_view_hoodie',
                  'back_view_hoodie',
                  'left_view_hoodie',
                  'right_view_hoodie'
                  ]


class BomberJacFrontSerializer(serializers.ModelSerializer):
    bomber_jac_body_front = ImageDetailSerializer()
    bomber_jac_collar_front = ImageDetailSerializer()
    bomber_jac_collar_inner_front = ImageDetailSerializer()
    bomber_jac_left_pocket_front = ImageDetailSerializer()
    bomber_jac_right_pocket_front = ImageDetailSerializer()
    bomber_jac_left_sleeve_front = ImageDetailSerializer()
    bomber_jac_right_sleeve_front = ImageDetailSerializer()
    bomber_jac_left_cuff_front = ImageDetailSerializer()
    bomber_jac_right_cuff_front = ImageDetailSerializer()
    bomber_jac_right_sleeve_design_front = ImageDetailSerializer()
    bomber_jac_hem_front = ImageDetailSerializer()
    bomber_jac_zip_front = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Front
        fields = ['id', 'name',
                  'bomber_jac_body_front',
                  'bomber_jac_collar_front',
                  'bomber_jac_collar_inner_front',
                  'bomber_jac_left_pocket_front',
                  'bomber_jac_right_pocket_front',
                  'bomber_jac_left_sleeve_front',
                  'bomber_jac_right_sleeve_front',
                  'bomber_jac_left_cuff_front',
                  'bomber_jac_right_cuff_front',
                  'bomber_jac_right_sleeve_design_front',
                  'bomber_jac_hem_front',
                  'bomber_jac_zip_front',

                  ]


class BomberJacBackSerializer(serializers.ModelSerializer):
    bomber_jac_body_back = ImageDetailSerializer()
    bomber_jac_collar_back = ImageDetailSerializer()
    bomber_jac_hem_back = ImageDetailSerializer()
    bomber_jac_left_sleeve_back = ImageDetailSerializer()
    bomber_jac_right_sleeve_back = ImageDetailSerializer()
    bomber_jac_left_cuff_back = ImageDetailSerializer()
    bomber_jac_right_cuff_back = ImageDetailSerializer()
    bomber_jac_left_sleeve_design_back = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Back
        fields = ['id', 'name',
                  'bomber_jac_body_back',
                  'bomber_jac_collar_back',
                  'bomber_jac_hem_back',
                  'bomber_jac_left_sleeve_back',
                  'bomber_jac_right_sleeve_back',
                  'bomber_jac_left_cuff_back',
                  'bomber_jac_right_cuff_back',
                  'bomber_jac_left_sleeve_design_back',
                  ]


class BomberJacLeftSerializer(serializers.ModelSerializer):
    bomber_jac_mid_body_left = ImageDetailSerializer()
    bomber_jac_left_body_left = ImageDetailSerializer()
    bomber_jac_right_body_left = ImageDetailSerializer()
    bomber_jac_bottom_body_left = ImageDetailSerializer()
    bomber_jac_left_cuff_left = ImageDetailSerializer()
    bomber_jac_right_cuff_left = ImageDetailSerializer()
    bomber_jac_mid_cuff_left = ImageDetailSerializer()
    bomber_jac_bottom_cuff_left = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Left
        fields = ['id', 'name',
                  'bomber_jac_mid_body_left',
                  'bomber_jac_left_body_left',
                  'bomber_jac_right_body_left',
                  'bomber_jac_bottom_body_left',
                  'bomber_jac_left_cuff_left',
                  'bomber_jac_right_cuff_left',
                  'bomber_jac_mid_cuff_left',
                  'bomber_jac_bottom_cuff_left',
                  ]


class BomberJacRightSerializer(serializers.ModelSerializer):
    bomber_jac_mid_body_right = ImageDetailSerializer()
    bomber_jac_left_body_right = ImageDetailSerializer()
    bomber_jac_right_body_right = ImageDetailSerializer()
    bomber_jac_bottom_body_right = ImageDetailSerializer()
    bomber_jac_left_cuff_right = ImageDetailSerializer()
    bomber_jac_right_cuff_right = ImageDetailSerializer()
    bomber_jac_mid_cuff_right = ImageDetailSerializer()
    bomber_jac_bottom_cuff_right = ImageDetailSerializer()

    class Meta:
        model = models.BomberJacket_Right
        fields = ['id', 'name',
                  'bomber_jac_mid_body_right',
                  'bomber_jac_left_body_right',
                  'bomber_jac_right_body_right',
                  'bomber_jac_bottom_body_right',
                  'bomber_jac_left_cuff_right',
                  'bomber_jac_right_cuff_right',
                  'bomber_jac_mid_cuff_right',
                  'bomber_jac_bottom_cuff_right',
                  ]


class BomberJacDetailSerializer(serializers.ModelSerializer):
    front_view_bomber_jac = BomberJacFrontSerializer()
    back_view_base_bomber_jac = BomberJacBackSerializer()
    left_view_bomber_jac = BomberJacLeftSerializer()
    right_view_bomber_jac = BomberJacRightSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name',
                  'front_view_bomber_jac',
                  'back_view_base_bomber_jac',
                  'left_view_bomber_jac',
                  'right_view_bomber_jac'
                  ]


class BaseBShirtFrontDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_body_front = ImageDetailSerializer()
    base_b_shirt_neck_front = ImageDetailSerializer()
    base_b_shirt_left_sleeve_front = ImageDetailSerializer()
    base_b_shirt_right_sleeve_front = ImageDetailSerializer()
    base_b_shirt_button_front = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Front
        fields = ['id', 'name',
                  'base_b_shirt_body_front',
                  'base_b_shirt_neck_front',
                  'base_b_shirt_left_sleeve_front',
                  'base_b_shirt_right_sleeve_front',
                  'base_b_shirt_button_front',
                  ]


class BaseBShirtBackDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_body_back = ImageDetailSerializer()
    base_b_shirt_left_sleeve_back = ImageDetailSerializer()
    base_b_shirt_right_sleeve_back = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Back
        fields = ['id', 'name',
                  'base_b_shirt_body_back',
                  'base_b_shirt_left_sleeve_back',
                  'base_b_shirt_right_sleeve_back',
                  ]


class BaseBShirtLeftDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_mid_left = ImageDetailSerializer()
    base_b_shirt_left_sleeve_left = ImageDetailSerializer()
    base_b_shirt_right_sleeve_left = ImageDetailSerializer()
    base_b_shirt_bottom_sleeve_left = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Left
        fields = ['id', 'name',
                  'base_b_shirt_mid_left',
                  'base_b_shirt_left_sleeve_left',
                  'base_b_shirt_right_sleeve_left',
                  'base_b_shirt_bottom_sleeve_left',
                  ]


class BaseBShirtRightDetailSerializer(serializers.ModelSerializer):
    base_b_shirt_mid_right = ImageDetailSerializer()
    base_b_shirt_left_sleeve_right = ImageDetailSerializer()
    base_b_shirt_right_sleeve_right = ImageDetailSerializer()
    base_b_shirt_bottom_sleeve_right = ImageDetailSerializer()

    class Meta:
        model = models.BaseBallShirt_Right
        fields = ['id', 'name',
                  'base_b_shirt_mid_right',
                  'base_b_shirt_left_sleeve_right',
                  'base_b_shirt_right_sleeve_right',
                  'base_b_shirt_bottom_sleeve_right',
                  ]


class BaseBShirtDetailSerializer(serializers.ModelSerializer):
    front_view_base_b_shirt = BaseBShirtFrontDetailSerializer()
    back_view_base_b_shirt = BaseBShirtBackDetailSerializer()
    left_view_base_b_shirt = BaseBShirtLeftDetailSerializer()
    right_view_base_b_shirt = BaseBShirtRightDetailSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name',
                  'front_view_base_b_shirt',
                  'back_view_base_b_shirt',
                  'left_view_base_b_shirt',
                  'right_view_base_b_shirt'
                  ]


class TankTopFrontSerializer(serializers.ModelSerializer):
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


class TankTopBackSerializer(serializers.ModelSerializer):
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


class TankTopDetailSerializer(serializers.ModelSerializer):
    front_view_tank_top = TankTopFrontSerializer()
    back_view_tank_top = TankTopBackSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name',
                  'front_view_tank_top',
                  'back_view_tank_top',
                  ]


class BagFrontSerializer(serializers.ModelSerializer):
    bag_handle_front = ImageDetailSerializer()
    bag_full_front_body = ImageDetailSerializer()
    bag_top_front_body = ImageDetailSerializer()
    bag_mid_front_body = ImageDetailSerializer()
    bag_bottom_front_body = ImageDetailSerializer()

    class Meta:
        model = models.BagFront
        fields = ['id', 'name',
                  'bag_handle_front',
                  'bag_full_front_body',
                  'bag_top_front_body',
                  'bag_mid_front_body',
                  'bag_bottom_front_body',
                  ]


class BagBackSerializer(serializers.ModelSerializer):
    bag_handle_back = ImageDetailSerializer()
    bag_full_back_body = ImageDetailSerializer()
    bag_top_back_body = ImageDetailSerializer()
    bag_mid_back_body = ImageDetailSerializer()
    bag_bottom_back_body = ImageDetailSerializer()

    class Meta:
        model = models.BagBack
        fields = ['id', 'name',
                  'bag_handle_back',
                  'bag_full_back_body',
                  'bag_top_back_body',
                  'bag_mid_back_body',
                  'bag_bottom_back_body',
                  ]


class BagDetailSerializer(serializers.ModelSerializer):
    front_view_bag = BagFrontSerializer()
    back_view_bag = BagBackSerializer()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name',
                  'front_view_bag',
                  'back_view_bag',
                  ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'display_image']


class CategoryListSerializer(serializers.ModelSerializer):
    designs = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'key', 'designs']

    def get_designs(self, obj):
        qs = models.ProductDesign.objects.filter(category=obj)
        serializer = ProductDesignWithCategorySerializers(qs, many=True)
        return serializer.data


class ProductDesignWithCategorySerializers(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductDesign
        fields = ['id', 'name', 'key', 'display_image']

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
