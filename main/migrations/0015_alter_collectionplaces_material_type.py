# Generated by Django 4.1.2 on 2023-03-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_collectionplaces_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionplaces',
            name='material_type',
            field=models.ManyToManyField(blank=True, related_name='collection_places', to='main.materialtype'),
        ),
    ]
