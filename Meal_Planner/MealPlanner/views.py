from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
import json

from .models import Recipe


# Create your views here.
def index(request):
    return render(request, 'MealPlanner/index.html')

def search(request):
    return render(request, 'MealPlanner/ingredients.html')

def random(request):
    return render(request, 'MealPlanner/randomRecipe.html')

def get_recipes(request, id):
    # if request.user.is_authenticated(): ... do stuff you would do if they were logged in
    # request.user will give you the user
    data = {'info': []}
    fav_recipes = get_object_or_404(Recipe, id=id, user=request.user)
    for recipe in fav_recipes:
        recipe_dict = {
            'id': recipe.recipe_id,
            'name': recipe.recipe_name
        }
        data['info'].append(recipe_dict)
    print(data)
    return JsonResponse(data)

def add_new_recipe(request):
    data = json.loads(request.body) 
    print(data)
    recipe_data = data.get('recipe')
    # print(recipe_data)
    new_id = recipe_data.get('id')
    new_name = recipe_data.get('title')
    Recipe.objects.create(recipe_id=new_id, recipe_name=new_name, user=request.user, recipe_info=recipe_data)
    return JsonResponse({'message': 'OK'})

# Have to create a view/button to save the ID of the recipe to a list
# Then have to call the list later and loop over it in a user profile
# Still have to create user model possibly with a ManytoMany relationship