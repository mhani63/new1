# Generated by Django 3.2.5 on 2021-09-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='star',
            field=models.BooleanField(default=False),
        ),
    ]
