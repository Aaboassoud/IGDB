# Generated by Django 4.0.4 on 2022-06-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesApp', '0002_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='image',
            field=models.URLField(blank=True, max_length=512),
        ),
    ]