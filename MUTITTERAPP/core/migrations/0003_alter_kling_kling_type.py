# Generated by Django 4.2.2 on 2023-09-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_klingreply_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kling',
            name='kling_type',
            field=models.CharField(choices=[('1', 'Hot'), ('2', 'Standard'), ('3', 'Relaxing')], max_length=1),
        ),
    ]
