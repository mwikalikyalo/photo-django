from django.db import models

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

