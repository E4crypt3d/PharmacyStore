# Generated by Django 4.2.7 on 2023-11-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_notification_alter_sale_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='is_notification',
            new_name='is_notified',
        ),
    ]