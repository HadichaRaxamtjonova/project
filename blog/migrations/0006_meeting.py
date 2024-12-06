# Generated by Django 5.1.4 on 2024-12-05 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('invitation', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('division', models.CharField(max_length=100)),
                ('first_text', models.TextField()),
                ('second_text', models.TextField()),
            ],
        ),
    ]