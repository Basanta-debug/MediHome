# Generated by Django 3.2.5 on 2021-08-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_auto_20210816_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]