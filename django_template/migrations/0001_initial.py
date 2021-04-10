# Generated by Django 3.2 on 2021-04-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=20)),
                ('book_author', models.CharField(max_length=20)),
                ('year_published', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Book Store',
                'verbose_name_plural': 'Book Store',
            },
        ),
    ]
