# Generated by Django 5.1.1 on 2024-09-05 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_lots_place'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BiddingCateories',
            new_name='BiddingCategories',
        ),
    ]