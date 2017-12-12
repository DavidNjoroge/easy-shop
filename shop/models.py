from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShopProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    latitude=models.FloatField()
    longitude=models.FloatField()
    imageprofile=models.ImageField(upload_to='profile/')
    shopname=models.CharField(max_length=50)

    def get_all_shops(self):
        all_shops=ShopProfile.objects.all()
        return all_shops

    @classmethod
    def get_shop(cls,shop_id):
        shop=ShopProfile.objects.filter(user=shop_id)
        return shop

    @classmethod
    def create_profile(cls,user,latitude,longitude,imageprofile,shopname):
        new_profile=ShopProfile(user=user,latitude=latitude,longitude=longitude,imageprofile=imageprofile,shopname=shopname)
        new_profile.save()
        return True