# Generated by Django 4.2.7 on 2023-11-11 15:00

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_notification_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='notification',
            managers=[
                ('notified', django.db.models.manager.Manager()),
            ],
        ),
    ]