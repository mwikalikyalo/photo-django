from unicodedata import category
from django.db import models
from categories.models import Category
from location.models import Location

# Create your models here.
class Image(models.model):
  image = models.ImageField()
  image_name = models.CharField(max_length= 200)
  image_description = models.CharField(max_length=1000)

  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
      return self.image

