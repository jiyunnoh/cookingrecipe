from django.shortcuts import render, get_object_or_404
from .models import Cuisine, Dietary, Difficulty, DishType, Occassion, Rating, Recipe, Review, Comment, Ingredient, Favorite

# Create your views here.
def index (request):
    return render(request, 'recipeapp/index.html')

def getrecipe(request):
    recipe_list=Recipe.objects.all()
    return render(request, 'recipeapp/recipe.html' ,{'recipe_list' : recipe_list})

def recipedetails(request, id):
    recipe=get_object_or_404(Recipe, pk=id)
    reviews=Review.objects.filter(recipe=id).count()
    context={
        'recipe' : recipe,
        'reviews': reviews,
    }
    return render(request, 'recipeapp/recipedetails.html', context=context)

def getcategory(request):
    return render(request, 'recipeapp/category.html')

def getdietary(request):
    dietary_list=Dietary.objects.all()
    return render(request, 'recipeapp/dietary.html', {'dietary_list' : dietary_list})

def getcuisine(request):
    cuisine_list=Cuisine.objects.all()
    return render(request, 'recipeapp/cuisine.html', {'cuisine_list' : cuisine_list})

def getdishtype(request):
    dishtype_list=DishType.objects.all()
    return render(request, 'recipeapp/dishtype.html', {'dishtype_list' : dishtype_list})

def getoccasion(request):
    occasion_list=Occassion.objects.all()
    return render(request, 'recipeapp/occasion.html', {'occasion_list' : occasion_list})