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

    def test_first_setup(self):
        self.first=ShopProfile(user=self.david,shopname='sdsdssd',imageprofile='sdsdfsfs')
        self.first.save()
        shops=ShopProfile.objects.all()
        self.assertTrue(len(shops)>0)
        
    def test_second_setup(self):
        self.first=ShopProfile(user=self.david,shopname='sdsdssd',imageprofile='sdsdfsfs')
        self.first.save()
        # self.second=ShopProfile(user=self.david,latitude=1234.2,longitude=12.54)
        # self.second.update()
        shop=ShopProfile.objects.get(user=self.david)
        shop.latitude=1234.2
        shop.longitude=12.54
        shop.save()
        self.assertEqual(shop.latitude,1234.2)