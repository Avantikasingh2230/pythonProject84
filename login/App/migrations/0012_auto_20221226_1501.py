# Generated by Django 3.2.16 on 2022-12-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20221224_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuecateringcombined',
            name='booking_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='venuecateringcombined',
            name='max_invitees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='venuecateringcombined',
            name='price_per_plate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='venuecateringcombined',
            name='tax_rate',
            field=models.IntegerField(),
        ),
    ]