from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role_type=models.CharField(max_length=40)

class ShopProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
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


class Movie:
    '''
    movie class to define movie objects
    '''
    def __init__(self,id,title,overview,image,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500'+image
        self.vote_average = vote_average
        self.vote_count = vote_count

class Media(models.Model):
    shop = models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    moviedb = models.IntegerField()

    @classmethod
    def get_shop_movies(cls,shop_id):
        shop=ShopProfile.objects.get(pk=shop_id)
        movies=Media.objects.filter(shop=shop)
        # movies=[]
        # for movie in movies:
        #     processed=get_movie(movie.id)
        #     movies.append(processed)
        return movies
