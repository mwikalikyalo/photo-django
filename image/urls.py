from unicodedata import name
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   #............
   path('', views.index, name="index"),
   path('category/<slug:category_slug>', views.category, name='category'),
   path('location/<slug:location_slug>', views.location, name='location'),
   path('search', views.search_images, name='search_images'),
   path('get-image/<int:id>/', views.get_image_by_id, name="get_image"),
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)