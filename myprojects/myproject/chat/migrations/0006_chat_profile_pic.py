# Generated by Django 4.2.16 on 2024-11-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_delete_login_chat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]