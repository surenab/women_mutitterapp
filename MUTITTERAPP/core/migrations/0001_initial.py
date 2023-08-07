# Generated by Django 4.2.2 on 2023-08-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cackling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField()),
                ('category', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=2000)),
                ('cackling_type', models.CharField(choices=[('1', 'Hot'), ('2', 'Standard'), ('3', 'Relaxing')], default='2', max_length=1)),
            ],
        ),
    ]
