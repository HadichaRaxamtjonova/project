# Generated by Django 5.1.4 on 2024-12-16 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_remove_customuser_name_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]