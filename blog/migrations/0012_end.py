# Generated by Django 5.1.4 on 2024-12-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_touch'),
    ]

    operations = [
        migrations.CreateModel(
            name='End',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
