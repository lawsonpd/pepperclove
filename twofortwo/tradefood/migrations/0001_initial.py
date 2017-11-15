# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 22:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('retail_value', models.FloatField(blank=True)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_phone', models.CharField(max_length=16)),
                ('accepted', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.FloatField(choices=[(0.020833333333333332, '30 minutes'), (0.041666666666666664, '1 hour'), (0.08333333333333333, '2 hours'), (0.125, '3 hours')], default=0.041666666666666664)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=16)),
                ('street_address', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=5)),
                ('joined', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('RESTAURANT', 'Restaurant'), ('GEN FOOD', 'Food')], default='RESTAURANT', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('retail_value', models.FloatField(blank=True)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_phone', models.CharField(max_length=16)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.FloatField(choices=[(0.020833333333333332, '30 minutes'), (0.041666666666666664, '1 hour'), (0.08333333333333333, '2 hours'), (0.125, '3 hours')], default=0.041666666666666664)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradefood.Merchant')),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradefood.Merchant'),
        ),
        migrations.AddField(
            model_name='bid',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradefood.Offer'),
        ),
    ]
