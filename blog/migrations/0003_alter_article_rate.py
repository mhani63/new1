# Generated by Django 3.2.5 on 2021-09-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rate',
            field=models.TextField(default=False),
        ),
    ]
