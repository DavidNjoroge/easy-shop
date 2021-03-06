from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('ajax/all_shops/',views.ShopList.as_view()),
    path('shop/<int:shop_id>',views.shop,name='shop'),
    path('setup/',views.setup,name='setup'),
    path('setup/next/',views.next),
    path('ajax/setup/',views.ajax_setup),
    path('myshop/',views.myshop,name='myshop'),
    path('subscribe/<int:shop_id>',views.subscribe,name='subscribe'),
    path('search/',views.search,name='search'),
    path('add_movie/<int:moviedb>',views.add_movie,name='add_movie'),
    path('delete/<int:media_id>',views.delete,name='delete')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)