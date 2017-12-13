from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('ajax/all_shops/',views.ShopList.as_view()),
    path('shop/<int:shop_id>',views.shop,name='shop'),
    path('accounts/',include('registration.backends.simple.urls')),
    path('setup/',views.setup,name='setup')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)