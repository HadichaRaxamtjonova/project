# Generated by Django 5.1.4 on 2024-12-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_remove_meeting_category_remove_meeting_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='photo',
            field=models.ImageField(default=1, upload_to='meeting_post/'),
            preserve_default=False,
        ),
    ]