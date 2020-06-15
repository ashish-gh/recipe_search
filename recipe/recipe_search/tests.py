from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home
from .views import recipe, new_review
from .models import Recipe

class HomeTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name='Chicken Roast', timing=40, direction="Cook at last", ingridents = "chicken", description='Cook in oven')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        recipe_topic_url = reverse('recipe', kwargs={'pk': self.recipe.pk})
        self.assertContains(self.response, 'href="{0}"'.format(recipe_topic_url))
    


class RecipeTopicTests(TestCase):
    def setUp(self):
        Recipe.objects.create(name='Chicken Roast', timing=40, direction="Cook at last", ingridents = "chicken", description='Cook in oven')

    def test_recipe_view_success_status_code(self):
        url = reverse('recipe', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_recipe_view_not_found_status_code(self):
        url = reverse('recipe', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_recipe_url_resolves_recipe_view(self):
        view = resolve('/recipe/1/')
        self.assertEquals(view.func, recipe)

    def test_recipe_view_contains_link_back_to_homepage(self):
        recipe_topic_url = reverse('recipe', kwargs={'pk': 1})
        response = self.client.get(recipe_topic_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    

class NewTopicTests(TestCase):
    def setUp(self):
        Recipe.objects.create(name='Chicken Roast', timing=40, direction="Cook at last", ingridents = "chicken", description='Cook in oven')

    def test_new_review_view_success_status_code(self):
        url = reverse('new_review', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_review_view_not_found_status_code(self):
        url = reverse('new_review', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_review_url_resolves_new_review_view(self):
        view = resolve('/recipe/1/new/')
        self.assertEquals(view.func, new_review)

    # def test_new_review_view_contains_link_back_to_recipe_view(self):
    #     new_review_url = reverse('new_review', kwargs={'pk': 1})
    #     recipe_url = reverse('recipe', kwargs={'pk': 1})
    #     response = self.client.get(new_review_url)
    #     self.assertContains(response, 'href="{0}"'.format(recipe_url))

    def test_recipe_topic_view_contains_navigation_links(self):
        recipe_topic_url = reverse('recipe', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_review', kwargs={'pk': 1})

        response = self.client.get(recipe_topic_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))