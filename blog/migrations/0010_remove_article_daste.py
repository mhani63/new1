# Generated by Django 3.2.5 on 2021-10-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211010_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='daste',
        ),
    ]
