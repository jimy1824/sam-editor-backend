from django.db import models
from constructor.models import TimeStampedModel, CustomUser


# Create your models here.


class LogosCategory(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Logo Category Name")

    def __str__(self):
        return f"{self.name}"


class SublimationCategory(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Sublimation Category Name")

    def __str__(self):
        return f"{self.name}"


class PrintingMethod(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Printing Method Name")

    def __str__(self):
        return f"{self.name}"


class PresetLogos(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Logo Name")
    category = models.ForeignKey(LogosCategory, on_delete=models.CASCADE, related_name='logos_category')
    printing_method = models.ManyToManyField(PrintingMethod)
    image = models.ImageField(upload_to='uploads/preset_logos')

    def __str__(self):
        return f"{self.name}"


class PresetSublimationPatterns(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Sublimation Name")
    category = models.ForeignKey(SublimationCategory, on_delete=models.CASCADE, related_name='sublimation_category')
    printing_method = models.ManyToManyField(PrintingMethod)
    image = models.ImageField(upload_to='uploads/preset_logos')

    def __str__(self):
        return f"{self.name}"


class UserLogo(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="Logo name")
    image = models.ImageField(upload_to='uploads/user')

    class Meta:
        verbose_name = 'Customer Graphics'
        verbose_name_plural = 'Customer Graphics'
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
