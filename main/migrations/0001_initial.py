# Generated by Django 3.2.16 on 2023-05-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default='Title')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
