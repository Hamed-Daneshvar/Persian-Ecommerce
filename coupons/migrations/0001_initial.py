# Generated by Django 3.2.15 on 2022-09-18 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Code')),
                ('valid_from', models.DateTimeField(verbose_name='Valid from')),
                ('valid_to', models.DateTimeField(verbose_name='Valid to')),
                ('discount', models.IntegerField(help_text='Percentage value (0 to 100)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
