# Generated by Django 3.1.1 on 2020-10-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='ratingstar',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]