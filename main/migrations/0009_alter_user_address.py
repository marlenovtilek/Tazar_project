# Generated by Django 4.1.2 on 2022-11-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_collectionplaces_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True, verbose_name='Адрес прожвания'),
        ),
    ]
