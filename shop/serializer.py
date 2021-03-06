from rest_framework import serializers
from .models import ShopProfile

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProfile
        fields=('id','latitude','longitude','shopname')