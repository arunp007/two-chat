# Generated by Django 4.0.1 on 2022-10-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'chat1',
            },
        ),
        migrations.CreateModel(
            name='Chat2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text2', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'chat2',
            },
        ),
    ]
