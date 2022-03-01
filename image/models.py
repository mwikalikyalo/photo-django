from unicodedata import category
from django.db import models
from .models import Category,Location

# Create your models here.
class Image(models.Model):
  image = models.ImageField()
  image_name = models.CharField(max_length= 200)
  image_description = models.CharField(max_length=1000)

  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
  def save_image(self):
        self.save()

  def delete_image(self):
        self.delete()

  @classmethod
  def update_image(cls, id, value):
        image = cls.objects.filter(id=id).update(image=value)

  @classmethod
  def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

  @classmethod
  def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

  @classmethod
  def filter_by_location(cls, location):
        images = Image.objects.filter(name=location).all()
        return images

  def __str__(self) -> str:
      return self.image

# order images from latest
class Meta:
    ordering = ['-date_posted'] 
