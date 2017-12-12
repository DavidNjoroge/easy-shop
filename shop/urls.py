from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('ajax/all_shops/',views.ShopList.as_view()),
    path('shop/<int:shop_id>',views.shop,name='shop')
]