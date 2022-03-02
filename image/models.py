from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):

  category_name = models.CharField(max_length=100)
  category_slug = models.CharField(max_length=50)
  category_description = models.CharField(max_length=1000)
  created_at = models.DateField(auto_now=True)

  def save_category(self):
        self.save()

  def delete_category(self):
        self.delete()

  def __str__(self) -> str:
      return self.category_name

#location
class Location(models.Model):
  location_name = models.CharField(max_length=100)
  location_slug = models.CharField(max_length=50)
  location_description = models.CharField(max_length=1000)

  def save_location(self):
        self.save()

  def delete_location(self):
        self.delete()
      
  def __str__(self) -> str:
    return self.location_name

# Create your models here.
class Image(models.Model):
  # image = models.ImageField()
  image_name = models.CharField(max_length= 200)
  image_description = models.CharField(max_length=1000)
  image = CloudinaryField('image')
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
      return self.image_name

# order images from latest
class Meta:
    ordering = ['-date_posted'] 
