# Generated by Django 5.0.6 on 2024-06-13 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_description_alter_listing_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='price',
            new_name='startingbid',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='imageUrl',
            new_name='url',
        ),
    ]
