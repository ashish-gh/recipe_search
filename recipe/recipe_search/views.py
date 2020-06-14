from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})
