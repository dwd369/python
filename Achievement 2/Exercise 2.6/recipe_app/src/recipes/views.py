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
from django.views.generic import ListView, DetailView, View
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   return render(request,'recipes/home_recipes.html')
   
class RecipeListView(LoginRequiredMixin,ListView):
   model = Recipe
   template_name = 'recipes/recipes.html'

class RecipeDetailView(LoginRequiredMixin,DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'
