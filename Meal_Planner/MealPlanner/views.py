from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json

from .models import Recipe

def index(request):
    return render(request, 'MealPlanner/index.html')

def search(request):
    return render(request, 'MealPlanner/ingredients.html')

def random(request):
    return render(request, 'MealPlanner/randomRecipe.html')

def profile_page(request):
    recipes = request.user.favorite_recipes.all()
    context = {'recipes' : recipes,}
    return render(request, 'MealPlanner/profile_page.html', context)

def recipe_details(request, id):
    recipes = request.user.favorite_recipes.all()
    selected_recipe = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'recipes' : recipes,
        'selected_recipe' : selected_recipe}
    return render(request, 'MealPlanner/recipeInfo.html', context)


def get_recipes(request, id):
    data = {'info': []}
    fav_recipes = get_object_or_404(Recipe, id=id, user=request.user)
    for recipe in fav_recipes:
        recipe_dict = {
            'id': recipe.recipe_id,
            'name': recipe.recipe_name
        }
        data['info'].append(recipe_dict)
    return JsonResponse(data)

def add_new_recipe(request):
    data = json.loads(request.body) 
    recipe_data = data.get('recipe')
    new_id = recipe_data.get('id')
    new_name = recipe_data.get('title')
    Recipe.objects.create(recipe_id=new_id, recipe_name=new_name, user=request.user, recipe_info=recipe_data)
    return JsonResponse({'message': 'OK'})

def delete_recipe(request, id):
    Recipe.objects.filter(id=id).delete()
    return redirect('MealPlanner:profile')
