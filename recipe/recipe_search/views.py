# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404
from django.contrib.auth.models import User
from .models import Recipe, Review


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})

def new_review(request, pk):
    new_review = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        user = User.objects.first()  # TODO: get the currently logged in user
        
        review = Review.objects.create(
            review=subject,
            recipe=new_review,
            created_by=user,
            updated_by = user
        )

        return redirect('recipe', pk = new_review.pk)  # TODO: redirect to the created topic page
    return render(request, 'new_recipe.html', {'new_review': new_review})    