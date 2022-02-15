from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'MealPlanner/ingredients.html')

def random(request):
    return render(request, 'MealPlanner/randomRecipe.html')