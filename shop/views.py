from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShopProfile,Media,Subscribe
from .serializer import ShopsSerializer
from .request import get_movie,get_movie_shop
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ShopProfileForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    medias=Media.objects.all()
    # processed_medias=[]
    # for media in medias:
    #     movies=get_movie_shop(media)
    #     processed_medias.append(movies)
    return render(request,'index.html',{'medias':medias})

def shops(request):
    data=[
        {'name':"bugatti"},
        {'name':"ferrari"},
        {'name':"mclaren"}
    ]
    return Response(data)
def setup(request):
    form=ShopProfileForm()
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
    shop=ShopProfile.objects.get(user=request.user)
    shop.latitude=lat
    shop.longitude=lng
    shop.save()
    return JsonResponse(data)
@login_required(login_url='/accounts/login/')
def next(request):
    if request.method=='POST':
            
        form=ShopProfileForm(request.POST,files=request.FILES)
        current_user=request.user
    
        if form.is_valid():
            
            new_shop=ShopProfile(user=request.user,shopname=form.data['shopname'],imageprofile=form.files['imageprofile'])
            new_shop.save()
            # form.user=current_user
            # form.save()
            print(form.data['shopname'])
    return render(request,'setupnext.html')

def myshop(request,user_id):
    return render(request,'myshop.html')

def subscribe(request,shop_id):
    shop=ShopProfile.objects.get(pk=shop_id)
    new_subscriber=Subscribe(shop=shop,user=request.user)
    new_subscriber.save()
    return redirect('/shop/'+str(shop_id))