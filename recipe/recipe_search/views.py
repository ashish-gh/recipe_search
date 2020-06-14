# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})
    