# Generated by Django 5.0.6 on 2024-06-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='url',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]
