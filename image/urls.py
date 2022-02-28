from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.display, name='search_results')
]