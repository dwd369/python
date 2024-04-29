# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Recipe

# # Create your views here.
# class RecipeListView(ListView):
#    model = Recipe
#    template_name = 'recipes/home_recipes.html'


# # def home(request):
# #    return render(request, 'recipes/home_recipes.html')



from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
   model = Recipe
   template_name = 'recipes/home_recipes.html'

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

