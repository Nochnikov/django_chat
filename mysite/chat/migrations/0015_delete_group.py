# Generated by Django 5.0.3 on 2024-05-24 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_group_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
