# Generated by Django 3.2.4 on 2021-07-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0014_designimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designimages',
            name='des_image',
        ),
        migrations.AddField(
            model_name='designimages',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/body'),
            preserve_default=False,
        ),
    ]
