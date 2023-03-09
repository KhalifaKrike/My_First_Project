# Generated by Django 4.1.4 on 2023-01-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30, verbose_name='Family Name')),
                ('SecondName', models.CharField(max_length=30, verbose_name='Name')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
