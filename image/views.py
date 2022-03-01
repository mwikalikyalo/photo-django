
from django.shortcuts import render
from .models import Location, Category, Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html', {'images':images, 'categories':categories, 'locations':locations})

def category(request, category_slug):
    category = Category.search_by_category(category_slug)
    images = Image.filter_by_category(category)
    return render(request, 'image.html', {'images':images, 'title': category})

def location(request, location_slug):
    location = Location.filter_by_location(location_slug)
    images = Image.filter_by_location(location)
    return render(request, 'image.html', {'images':images, 'title': location}) 

def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "display.html", {"image": image})

def search_images(request):

    if 'images' in request.GET and request.GET["images"]:
        category = request.GET.get("images")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})