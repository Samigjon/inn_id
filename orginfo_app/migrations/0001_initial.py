# Generated by Django 4.2.15 on 2024-08-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tin', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=255)),
                ('registration_date', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
