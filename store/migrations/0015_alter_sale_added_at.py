# Generated by Django 4.2.7 on 2023-11-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_sale_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='added_at',
            field=models.DateTimeField(),
        ),
    ]
