# Generated by Django 4.2.4 on 2023-08-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_kling_category_kling_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kling',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/img'),
        ),
    ]
