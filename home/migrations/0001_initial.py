# Generated by Django 4.2.13 on 2024-07-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.ImageField(upload_to='number_plate/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
