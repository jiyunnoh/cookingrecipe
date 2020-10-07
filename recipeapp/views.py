from django.shortcuts import render
from .models import Cuisine, Dietary, Difficulty, DishType, Occassion, Rating, Recipe, Review, Comment, Ingredient, Favorite

# Create your views here.
def index (request):
    return render(request, 'recipeapp/index.html')

def getrecipe(request):
    recipe_list=Recipe.objects.all()
    return render(request, 'recipeapp/recipe.html' ,{'recipe_list' : recipe_list})
    