from . import views
from django.urls import path

urlpatterns=[
   #............
    path('search/', views.search_results, name='search_results')
]