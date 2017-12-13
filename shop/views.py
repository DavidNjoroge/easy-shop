from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShopProfile,Media
from .serializer import ShopsSerializer
from .request import get_movie

# Create your views here.
def index(request):
    return render(request,'index.html')

def shops(request):
    data=[
        {'name':"bugatti"},
        {'name':"ferrari"},
        {'name':"mclaren"}
    ]
    return Response(data)
def setup(request):
    return render(request,'setup.html')
class ShopList(APIView):
    def get(self,request,format=None):
        all_shops=ShopProfile.objects.all()
        serializers=ShopsSerializer(all_shops,many=True)
        return Response(serializers.data)

def shop(request,shop_id):
    
    shop = ShopProfile.objects.get(pk=shop_id)
    movies=Media.get_shop_movies(shop_id)
    medias=[]
    for movie in movies:
        processed=get_movie(movie.moviedb)
        medias.append(processed)
    print(len(medias))
    return render(request,'shop.html',{'shop':shop,'medias':medias})