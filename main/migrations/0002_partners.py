# Generated by Django 4.1.2 on 2022-11-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='main/static/img/')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование организации')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес организации')),
                ('phone', models.CharField(max_length=15, verbose_name='Контакты организации')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
