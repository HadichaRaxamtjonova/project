# Generated by Django 5.1.4 on 2024-12-14 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_user_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popular',
            name='text',
        ),
    ]