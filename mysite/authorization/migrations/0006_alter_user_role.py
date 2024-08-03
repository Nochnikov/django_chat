# Generated by Django 5.0.3 on 2024-05-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_remove_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'admin'), (2, 'moderator'), (3, 'user')], default=3),
        ),
    ]