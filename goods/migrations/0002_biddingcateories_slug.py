# Generated by Django 4.2.14 on 2024-07-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biddingcateories',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
    ]