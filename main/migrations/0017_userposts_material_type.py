# Generated by Django 4.1.2 on 2023-04-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_userposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userposts',
            name='material_type',
            field=models.ManyToManyField(blank=True, related_name='user_collection_places', to='main.materialtype'),
        ),
    ]
