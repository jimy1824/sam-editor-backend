# Generated by Django 3.2.4 on 2021-06-10 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_auto_20210610_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='body_view',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='body_view', to='constructor.imagefield'),
            preserve_default=False,
        ),
    ]
