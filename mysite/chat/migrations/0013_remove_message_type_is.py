# Generated by Django 5.0.3 on 2024-05-04 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_alter_privatechat_table_alter_publicchat_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='type_is',
        ),
    ]