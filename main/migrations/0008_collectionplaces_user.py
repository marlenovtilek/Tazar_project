# Generated by Django 4.1.2 on 2022-11-29 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionplaces',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_places', to=settings.AUTH_USER_MODEL),
        ),
    ]
