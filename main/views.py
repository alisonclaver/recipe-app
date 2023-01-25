from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'main/home.html', context)

def recipes_page(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, 'main/recipes.html', context)

def onerecipe_page(request, pk):
    recipes = Recipe.objects.get(id=pk)
    context = {'recipes':recipes}
    return render(request, 'main/onerecipe.html', context)