from django.urls import path, include
from . import views
from .views import RecipeListView, RecipeDetailView, records
# , recipelist, recipedetails

app_name = 'recipes'

urlpatterns = [
   path('', views.home, name='home'),
   path('search', views.records, name='search'),
   path('recipes/', RecipeListView.as_view(), name='list'),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]