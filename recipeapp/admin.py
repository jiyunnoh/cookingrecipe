from django.contrib import admin
from .models import Cuisine, Dietary, Difficulty, DishType, Occassion, Rating, Recipe, Review, Comment, Ingredient, Favorite

# Register your models here.
admin.site.register(Cuisine)
admin.site.register(Dietary)
admin.site.register(Difficulty)
admin.site.register(DishType)
admin.site.register(Occassion)
admin.site.register(Rating)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Favorite)