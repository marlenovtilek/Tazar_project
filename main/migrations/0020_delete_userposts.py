# Generated by Django 4.1.2 on 2023-05-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_collectionplaces_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPosts',
        ),
    ]
