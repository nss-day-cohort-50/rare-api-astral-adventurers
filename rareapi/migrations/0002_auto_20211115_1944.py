# Generated by Django 3.2.9 on 2021-11-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
