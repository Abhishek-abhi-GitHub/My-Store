# Generated by Django 4.1.2 on 2022-11-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=999)),
                ('category', models.CharField(max_length=999)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
