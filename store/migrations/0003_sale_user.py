# Generated by Django 4.2.7 on 2023-11-07 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Sold', to=settings.AUTH_USER_MODEL),
        ),
    ]