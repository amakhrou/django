# Generated by Django 4.2.16 on 2024-11-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_chat_joined_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='display_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]