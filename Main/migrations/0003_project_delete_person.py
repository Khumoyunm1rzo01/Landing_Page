# Generated by Django 4.0.1 on 2022-02-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='rasm/')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
