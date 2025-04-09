# Generated by Django 3.1.7 on 2021-03-06 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210304_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pred_result',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
