# Generated by Django 3.1.3 on 2020-11-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradefood', '0003_auto_20171203_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]