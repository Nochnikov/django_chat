# Generated by Django 5.0.3 on 2024-04-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_profile_user_id_alter_message_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatspace',
            name='chat_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chatspace',
            name='is_private',
            field=models.CharField(choices=[(1, 'Private'), (2, 'Group')]),
        ),
    ]
