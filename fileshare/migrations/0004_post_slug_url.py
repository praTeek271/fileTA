# Generated by Django 5.0.3 on 2024-03-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0003_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
