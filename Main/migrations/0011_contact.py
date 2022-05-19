# Generated by Django 4.0.1 on 2022-02-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('subject', models.CharField(max_length=355)),
                ('message', models.TextField()),
            ],
        ),
    ]
