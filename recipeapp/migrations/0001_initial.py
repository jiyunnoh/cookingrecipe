# Generated by Django 3.1.1 on 2020-10-01 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisinename', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'cuisines',
                'db_table': 'cuisine',
            },
        ),
        migrations.CreateModel(
            name='Dietary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dietarytype', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'dietary types',
                'db_table': 'dietary',
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficultylevel', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'difficulty levels',
                'db_table': 'difficulty',
            },
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishtypename', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'dishtypes',
                'db_table': 'dishtype',
            },
        ),
        migrations.CreateModel(
            name='Occassion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occassiontype', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'occassions',
                'db_table': 'occassion',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'ratings',
                'db_table': 'rating',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipename', models.CharField(max_length=255)),
                ('recipedescription', models.CharField(max_length=255)),
                ('recipeinstruction', models.TextField()),
                ('servingsize', models.SmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('preptime', models.TimeField()),
                ('cooktime', models.TimeField()),
                ('totaltime', models.TimeField()),
                ('cuisine', models.ManyToManyField(to='recipeapp.Cuisine')),
                ('dietary', models.ManyToManyField(to='recipeapp.Dietary')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.difficulty')),
                ('dishtype', models.ManyToManyField(to='recipeapp.DishType')),
                ('occassion', models.ManyToManyField(to='recipeapp.Occassion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'recipes',
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('reviewtext', models.TextField()),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.rating')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientname', models.CharField(max_length=255)),
                ('measurement', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
            ],
            options={
                'verbose_name_plural': 'ingredients',
                'db_table': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foldername', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'favorites',
                'db_table': 'favorite',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentdate', models.DateField()),
                ('commenttext', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'comments',
                'db_table': 'comment',
            },
        ),
    ]
