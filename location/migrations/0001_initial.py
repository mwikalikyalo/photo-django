# Generated by Django 4.0.2 on 2022-03-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('location_slug', models.CharField(max_length=50)),
                ('location_description', models.CharField(max_length=1000)),
            ],
        ),
    ]
