from django.urls import path
from . import views

app_name = 'MealPlanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('random/', views.random, name='random'),
    path('get-recipes/', views.get_recipes, name='getRecipe'),
    path('new/', views.add_new_recipe, name='newRecipe')
    
]
