from django.test import TestCase
from django.contrib.auth.models import User
from .models import ShopProfile

# Create your tests here.

class ShopProfileTextClass(TestCase):
    def setUp(self):
        self.david=User(username='david',password='sdfsdfsd')
        self.david.save()
        self.new_profile=ShopProfile(user=self.david,latitude=12.0,longitude=3.6,imageprofile='sdfs',shopname='sdfdsfsd')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,ShopProfile))
        
