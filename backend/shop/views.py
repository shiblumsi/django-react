from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import ShopSerializer, AddressSerializer
from .models import Shop, Address


# Create your views here.
class ShopCreateView(CreateAPIView):
    shops = Shop.objects.all()
    serializer_class = ShopSerializer


class AddressView(CreateAPIView):
    address = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        shop = Shop.objects.get(id=1)
        print(serializer)
        serializer.save(shop=shop)


        return serializer


