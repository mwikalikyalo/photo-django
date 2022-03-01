from django.db import models

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=100)
  location_slug = models.CharField(max_length=50)
  location_description = models.CharField(max_length=1000)

  def __str__(self) -> str:
      return self.location_name

  def save_location(self):
        self.save()

  def delete_location(self):
        self.delete()
