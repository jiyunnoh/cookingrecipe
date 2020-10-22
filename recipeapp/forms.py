from django import forms
from .models import Cuisine, Dietary, Difficulty, DishType, Occassion, Rating, Recipe, Review, Comment, Ingredient, Favorite

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields='__all__'