from django.test import TestCase
from .models import Category

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='earth', category_slug='earth',category_description='3rd planet in solar system', created_at='2:30pm, 28th Feb, 2022')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    # Testing save method
    def test_save(self):
        self.category.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    # Testing delete method
    def test_delete(self):
        self.category.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)