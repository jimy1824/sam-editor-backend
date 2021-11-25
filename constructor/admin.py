from django.contrib import admin
from django.utils.html import format_html

from constructor import models as ConstructorModels
from django import forms


# Register your models here.

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = ConstructorModels.CustomUser
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if len(self.cleaned_data["password"]) < 16:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(ConstructorModels.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = [field.name for field in ConstructorModels.CustomUser._meta.fields]
    ordering = ['id']
    search_fields = ['id', 'email']


@admin.register(ConstructorModels.Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Fabric._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    filter_horizontal = ('colors',)


@admin.register(ConstructorModels.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Color._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.ProductSizeModel._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.SizeFieldModel)
class SizeFieldModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.SizeFieldModel._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Category._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ComponentSelection)
class ComponentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.ComponentSelection._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ProductDesign)
class CategoryProductDesignAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'display_image_tag']
    ordering = ['id']
    search_fields = ('name',)
    filter_horizontal = ['fabrics', 'component_selected']
    change_form_template = 'admin/admin_customization.html'
    save_as = True

    def display_image_tag(self, obj):
        return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))


@admin.register(ConstructorModels.CoachJacket_Front)
class CoachJacket_FrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.CoachJacket_Front._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.CoachJacket_Left)
class CoachJacket_LeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.CoachJacket_Left._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.CoachJacket_Right)
class CoachJacket_RightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.CoachJacket_Right._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.CoachJacket_Back)
class CoachJacket_BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.CoachJacket_Back._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BomberJacket_Front)
class BomberJacket_FrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BomberJacket_Front._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BomberJacket_Left)
class BomberJacket_LeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BomberJacket_Left._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BomberJacket_Right)
class BomberJacket_RightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BomberJacket_Right._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BomberJacket_Back)
class BomberJacket_BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BomberJacket_Back._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.HoodieFront)
class HoodieFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HoodieFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.HoodieBack)
class HoodieBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HoodieBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.HoodieLeft)
class HoodieLeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HoodieLeft._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.HoodieRight)
class HoodieRightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HoodieRight._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Body._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.LeftView)
class LeftView(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.LeftView._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.RightView)
class RightView(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.RightView._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BackView)
class BackView(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BackView._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    # autocomplete_fields = ["back_first_part"]


@admin.register(ConstructorModels.DesignImages)
class DesignImages(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.DesignImages._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.TowelFront)
class TowelFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.TowelFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.TowelBack)
class TowelBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.TowelBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.Apron)
class ApronAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Apron._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.HatFront)
class HatFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HatFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.HatBack)
class HatBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HatBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.HatLeft)
class HatLeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HatLeft._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.HatRight)
class HatRightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.HatRight._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallShirt_Front)
class BaseBallShirt_FrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallShirt_Front._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallShirt_Left)
class BaseBallShirt_LeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallShirt_Left._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallShirt_Right)
class BaseBallShirt_RightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallShirt_Right._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallShirt_Back)
class BaseBallShirt_BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallShirt_Back._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallJacket_Front)
class BaseBallJacket_FrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallJacket_Front._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallJacket_Left)
class BaseBallJacket_LeftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallJacket_Left._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallJacket_Right)
class BaseBallJacket_RightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallJacket_Right._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.BaseBallJacket_Back)
class BaseBallJacket_BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BaseBallJacket_Back._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.PantFront)
class PantFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.PantFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.PantBack)
class PantBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.PantBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)
    list_display += ['display_image_url']

    def display_image_url(self, obj):
        try:
            return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.display_image.url))
        except:
            return


@admin.register(ConstructorModels.TankTop_Front)
class TankTop_FrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.TankTop_Front._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.TankTop_Back)
class TankTop_BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.TankTop_Back._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.VestFront)
class VestFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.VestFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.VestBack)
class VestBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.VestBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.ImageField)
class ImageFieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'x_point', 'y_point', 'display_image_tag']
    ordering = ['id']
    search_fields = ('name',)

    def display_image_tag(self, obj):
        return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.image.url))


@admin.register(ConstructorModels.BagBack)
class BagBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BagBack._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.BagFront)
class BagFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.BagFront._meta.fields]
    ordering = ['id']
    search_fields = ('name',)


@admin.register(ConstructorModels.Components)
class BagFrontAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.Components._meta.fields]
    ordering = ['id']
    search_fields = ('name', 'category', 'component')


@admin.register(ConstructorModels.UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConstructorModels.UserOrder._meta.fields]
    ordering = ['id']
    search_fields = ('user', 'product_design')
