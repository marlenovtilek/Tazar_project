# Generated by Django 4.1.2 on 2022-12-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_collectionplaces_user_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='description',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='full_name',
        ),
        migrations.AddField(
            model_name='volunteers',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='first_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя волонтера'),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='last_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Фамилия волонтера'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
