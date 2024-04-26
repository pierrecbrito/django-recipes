from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
    """
        Testes relativos a renderização da URL correta.
    """
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
    
    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(detail_url, '/recipes/1/')