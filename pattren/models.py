from django.db import models
from constructor.models import TimeStampedModel

# Create your models here.


class LogosCategory(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Logo Category Name")

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
