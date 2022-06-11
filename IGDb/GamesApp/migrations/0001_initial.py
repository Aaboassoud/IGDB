# Generated by Django 4.0.5 on 2022-06-11 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=124)),
                ('description', models.TextField(blank=True)),
                ('date_realeased', models.DateTimeField()),
                ('company', models.CharField(choices=[('Sony', 'Sony'), ('Microsoft', 'Microsoft'), ('Activision Blizzard', 'Activision Blizzard'), ('Electronic Arts', 'Electronic Arts'), ('Epic Games', 'Epic Games'), ('Ubisoft', 'Ubisoft')], max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modfiy', models.DateTimeField(auto_now=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]