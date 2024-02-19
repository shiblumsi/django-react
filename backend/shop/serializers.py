from rest_framework import serializers
from .models import Shop, Photo, Address
from api.models import Person


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [ 'thana', 'district', 'postal_code']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = ['shop']


class ShopSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    photo = PhotoSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['title', 'name', 'address', 'photo']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        photo_data = validated_data.pop('photo')
        person = Person.objects.get(id=1)
        shop = Shop.objects.create(shop_owner=person, **validated_data)
        Address.objects.create(shop=shop, **address_data)
        Photo.objects.create(shop=shop, **photo_data)

        return shop
