# Generated by Django 4.1.2 on 2023-03-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_partners_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionplaces',
            name='user',
        ),
        migrations.RemoveField(
            model_name='collectionplaces',
            name='working_from',
        ),
        migrations.RemoveField(
            model_name='collectionplaces',
            name='working_to',
        ),
        migrations.AddField(
            model_name='collectionplaces',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='collectionplaces',
            name='working_hours',
            field=models.CharField(max_length=100, null=True, verbose_name='График работы'),
        ),
        migrations.AlterField(
            model_name='collectionplaces',
            name='address',
            field=models.CharField(max_length=256, verbose_name='Адрес пункта'),
        ),
        migrations.AlterField(
            model_name='collectionplaces',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Наименование пункта'),
        ),
        migrations.AlterField(
            model_name='members',
            name='avatar',
            field=models.ImageField(upload_to='Фото участника'),
        ),
    ]
