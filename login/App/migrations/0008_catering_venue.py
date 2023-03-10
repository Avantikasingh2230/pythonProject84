# Generated by Django 3.2.16 on 2022-12-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20221222_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_plate', models.IntegerField(max_length=200)),
                ('tax_rate', models.IntegerField(max_length=200)),
                ('discounted_price', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_price', models.ImageField(max_length=200, upload_to='')),
                ('tax_rate', models.ImageField(max_length=200, upload_to='')),
                ('max_invitees', models.IntegerField(max_length=200)),
            ],
        ),
    ]
