from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShopProfile,Media
from .serializer import ShopsSerializer
from .request import get_movie
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ShopProfileForm
from django.contrib.auth.decorators import login_required



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
    form=ShopProfileForm
    return render(request,'setup.html',{'form':form})
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

@csrf_exempt
def ajax_setup(request):
    data={'success':'sdfssdssd'}
    lat=request.POST.get('lat')
    lng=request.POST.get('lng')
    # print()
    return JsonResponse(data)
@login_required(login_url='/accounts/login/')
def next(request):
    if request.method=='POST':
            
        form=ShopProfileForm(request.POST,request.FILES)
        print(request.user.id)
    
        if form.is_valid():
            form.user=request.user
            form.save()
            print('harrrooo')
    return render(request,'setupnext.html')