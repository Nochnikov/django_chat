# Generated by Django 5.0.3 on 2024-04-23 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_chatspace_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='subscriptions',
            new_name='users',
        ),
    ]