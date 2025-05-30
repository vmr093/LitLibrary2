# Generated by Django 5.1.6 on 2025-03-10 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('cover_image', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('want_to_read', 'Want to Read'), ('currently_reading', 'Currently Reading'), ('read', 'Read')], default='want_to_read', max_length=20)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
