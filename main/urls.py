from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('recipes/', views.recipes_page, name='recipes'),
    path('recipe/<str:pk>/', views.onerecipe_page, name='one_recipe'),
]