from django.db import models

# Create your models here.
class Image(models.model):
  image = models.ImageField()
  image_name = models.CharField(max_length= 200)
  image_description = models.CharField(max_length=1000)
  image_location_foreign_key = models.CharField(max_length=500)
  image_category_foreign_key = models.CharField(max_length=500)

  def __str__(self) -> str:
      return self.image

