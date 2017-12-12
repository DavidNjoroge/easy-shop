from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShopProfile
from .serializer import ShopsSerializer

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

class ShopList(APIView):
    def get(self,request,format=None):
        all_shops=ShopProfile.objects.all()
        serializers=ShopsSerializer(all_shops,many=True)
        return Response(serializers.data)

def shop(request,shop_id):
    return render(request,'shop.html')