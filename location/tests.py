from django.test import TestCase
from .models import Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Kenya', location_slug='ken', location_description='Country below Ethiopia')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    # Testing save method
    def test_save(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Testing delete method
    def test_delete(self):
        self.location.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)