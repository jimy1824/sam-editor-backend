from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Product Category Name")
    key = models.CharField(max_length=250, unique=True, help_text="Product Category Key")

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}-{self.key}"


class ImageField(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Image Name")
    image = models.ImageField(upload_to='uploads/body')
    x_point = models.IntegerField()
    y_point = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class Body(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Body Name")
    body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_view', )
    body_first_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_first_section',
                                           blank=True, null=True)
    body_second_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_second_section',
                                            blank=True, null=True)
    body_third_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_third_section',
                                           blank=True, null=True)
    collar = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar', blank=True, null=True)
    hem = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hem', blank=True,  null=True)
    right_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name = 'r_sleeve', blank=True, null=True)
    left_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name= 'l_sleeve')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class LeftView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Left View")
    left_v_body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_body_view',
                                          blank=True, null=True)
    left_v_upper_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_upper_part',
                                          blank=True, null=True)
    left_v_lower_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_lower_part',
                                           blank=True, null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class RightView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Right View")
    right_v_body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_body_view',
                                          blank=True, null=True)
    right_v_upper_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_upper_part',
                                           blank=True, null=True)
    right_v_lower_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_lower_part',
                                           blank=True, null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"

class BackView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Back View")
    back_first_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_first_part',
                                           blank=True, null=True)
    back_second_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_second_part',
                                           blank=True, null=True)
    back_third_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_third_part',
                                         blank=True, null=True)
    back_left_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_left_sleeve',
                                         blank=True, null=True)
    back_right_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_right_sleeve',
                                          blank=True, null=True)


    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"

class ProductDesign(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Product Design Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='uploads/display')
    front_view = models.ForeignKey(Body, on_delete=models.CASCADE)
    back_view = models.ForeignKey(BackView, on_delete=models.CASCADE)
    left_view = models.ForeignKey(LeftView, on_delete=models.CASCADE,null=True,blank=True)
    right_view = models.ForeignKey(RightView, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
