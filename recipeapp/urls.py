from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getrecipe/', views.getrecipe, name='recipe'),
    path('recipedetails/<int:id>', views.recipedetails, name='recipedetails'),
    path('getcategory/', views.getcategory, name='category'),
]