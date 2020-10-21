from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getrecipe/', views.getrecipe, name='recipe'),
    path('recipedetails/<int:id>', views.recipedetails, name='recipedetails'),
    path('getcategory/', views.getcategory, name='category'),
    path('occasion/', views.getoccasion, name='occasion'),
    path('dietary/', views.getdietary, name='dietary'),
    path('cuisine/', views.getcuisine, name='cuisine'),
    path('dishtype/', views.getdishtype, name='dishtype'),
]