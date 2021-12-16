# Generated by Django 3.2.5 on 2021-08-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0011_auto_20210810_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_comlpeted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_method',
            field=models.CharField(choices=[('cod', 'Cash On Delivery'), ('Khalti', 'Khalti')], default='Cash On Delivery', max_length=20),
        ),
    ]
