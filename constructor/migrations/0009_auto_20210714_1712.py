# Generated by Django 3.2.4 on 2021-07-14 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0008_remove_hatfront_hat_full_body_front'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hatback',
            name='hat_full_body_back',
        ),
        migrations.RemoveField(
            model_name='hatleft',
            name='hat_full_body_left',
        ),
        migrations.RemoveField(
            model_name='hatright',
            name='hat_full_body_right',
        ),
    ]
