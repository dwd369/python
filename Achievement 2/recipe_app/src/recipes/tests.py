from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Tea', cook_time = 5, ingredients = 'tea leaves, water', description = 'Boil water and add tea leaves, brew for 5 minutes.')
    
    def test_recipe_name(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')


    def test_author_name_max_length(self):
        # Get a book object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)


    def test_recipe_cook_time(self):
        # Get a book object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('cook_time').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'cook time')

    def test_recipe_cook_ingredients(self):
        # Get a book object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('ingredients').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'ingredients')
    
    def test_get_absolute_url(self):
        book = Recipe.objects.get(id=1)
        #get_absolute_url() should take you to the detail page of book #1
        #and load the URL /books/list/1
        self.assertEqual(book.get_absolute_url(), '/recipes/list/1')