from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd

# Create your views here.

def home(request):
   return render(request,'recipes/home_recipes.html')
   
def records(request):
   form = RecipeSearchForm(request.POST or None)
   # recipes_df = None
   # chart = None

   if request.method == 'POST':
      #read recipes and chart_type
      recipe_name = request.POST.get('recipe_name')
      chart_type = request.POST.get('chart_type')

      print(recipe_name, chart_type)
      context = {
         'form': form,
      }

      return render(request, 'recipes/recipes_search.html')
   # check if the button is clicked
   # if request.method == 'POST':
   #    #read recipes and chart_type
   #    recipe_name = request.POST.get('recipe_name')
   #    chart_type = request.POST.get('chart_type')

   #    # apply filter to extract data
   #    qs = Recipe.objects.filter(recipe__name = recipe_name)
   #    if qs:
   #       # convert queryset values to pandas dataframe
   #       recipes_df = pd.DataFrame(qs.values())

   #       print(recipe)



class RecipeListView(LoginRequiredMixin,ListView):
   model = Recipe
   template_name = 'recipes/recipes.html'

class RecipeDetailView(LoginRequiredMixin,DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'