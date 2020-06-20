# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404
from django.contrib.auth.models import User
from .models import Recipe, Review
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# 
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})
# 
def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})

# 
@login_required
def new_review(request, pk):
    new_review = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        user = User.objects.first()  # TODO: get the currently logged in user
        
        review = Review.objects.create(
            review=subject,
            recipe=new_review,
            created_by=request.user,
            updated_by = user
        )

        return redirect('recipe', pk = new_review.pk)  # TODO: redirect to the created topic page
    return render(request, 'new_recipe.html', {'new_review': new_review})    


# 
def recipe_review(request, pk, review_pk):
    print(pk, review_pk)
    reviews = get_object_or_404(Review, recipe_id=pk, pk=review_pk)
    print("reviews id: ", reviews.id)
    print("review: ", reviews.review)
    return render(request, 'recipe_review.html', {'reviews': reviews})


# reply review
@login_required
def reply_review(request, pk, review_pk):
    review = get_object_or_404(Review, recipe_id=pk, pk=review_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.review = review
            # post.created_by = request.user
            # post.save()
            return redirect('recipe_review', pk=pk, review_pk=review_pk)
    else:
        form = PostForm()
    return render(request, 'reply_review.html', {'reviews': review, 'form': form})