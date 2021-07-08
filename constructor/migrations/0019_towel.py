# Generated by Django 3.2.4 on 2021-07-08 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0018_auto_20210707_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Towel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Towel Front', max_length=250)),
                ('towel_back', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towel_back', to='constructor.imagefield')),
                ('towel_front', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towel_front', to='constructor.imagefield')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
    ]
