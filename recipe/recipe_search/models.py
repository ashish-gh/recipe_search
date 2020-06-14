from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    timing = models.IntegerField()
    direction =  models.CharField(max_length=500)
    ingridents = models.CharField(max_length=500)
    description = models.CharField(max_length=500)


class Review(models.Model):
    review = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    rated_by = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
