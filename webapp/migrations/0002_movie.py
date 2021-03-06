# Generated by Django 3.0.7 on 2020-06-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=120)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=120)),
                ('writers', models.CharField(max_length=120)),
                ('stars', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
