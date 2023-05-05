# Generated by Django 4.1.2 on 2023-04-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_userposts_material_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userposts',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='collectionplaces',
            name='material_type',
            field=models.ManyToManyField(blank=True, to='main.materialtype'),
        ),
        migrations.AlterField(
            model_name='collectionplaces',
            name='photo',
            field=models.ImageField(null=True, upload_to='collection_places', verbose_name='Картинка'),
        ),
    ]
