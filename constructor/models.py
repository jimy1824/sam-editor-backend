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
    collar = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar')
    hem = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hem')

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

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
