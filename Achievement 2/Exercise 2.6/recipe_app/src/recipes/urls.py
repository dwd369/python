from django.urls import path, include
from . import views
from .views import RecipeListView, RecipeDetailView
# , recipelist, recipedetails

app_name = 'recipes'

urlpatterns = [
   # path('list/', recipelist),
   # path('list/<pk>', recipedetails),
   path('', views.home, name='home'),
   path('recipes/', RecipeListView.as_view(), name='list'),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]