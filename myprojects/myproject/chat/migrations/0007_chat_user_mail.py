# Generated by Django 4.2.16 on 2024-11-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_chat_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='user_mail',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
