from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def shops(request):
    data=[
        {'name':"bugatti"},
        {'name':"ferrari"},
        {'name':"mclaren"}
    ]
    return JsonResponse(data)