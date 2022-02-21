from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

from .models import Recipe


# Create your views here.
def index(request):
    return render(request, 'MealPlanner/ingredients.html')

def random(request):
    return render(request, 'MealPlanner/randomRecipe.html')

def get_todos(request):
    data = {'info': []}
    fav_recipes = Recipe.objects.all()
    for recipe in fav_recipes:
        recipe_dict = {
            'id': recipe.recipe_id,
            'name': recipe.recipe_name
        }
        data['info'].append(recipe_dict)
    print(data)
    return JsonResponse(data)

def add_new_todo(request):
    data = json.loads(request.body) # request.body is the data property of the axios call
    # it comes in as a string, so json.loads take in that string and returns a python dictionary
    # print(data) # {'text': 'test'}
    new_id = data.get('id')
    Recipe.objects.create(recipe_id=new_id)
    return JsonResponse({'message': 'OK'})

# Have to create a view/button to save the ID of the recipe to a list
# Then have to call the list later and loop over it in a user profile
# Still have to create user model possibly with a ManytoMany relationship