from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'MealPlanner/ingredients.html')

def random(request):
    return render(request, 'MealPlanner/randomRecipe.html')


# Have to create a view/button to save the ID of the recipe to a list
# Then have to call the list later and loop over it in a user profile
# Still have to create user model possibly with a ManytoMany relationship