# Generated by Django 4.1.6 on 2023-09-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='creditcard',
            field=models.IntegerField(blank=True),
        ),
    ]