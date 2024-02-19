from django.db import models
from autoslug import AutoSlugField

from api.models import Person


class Shop(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    shop_owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Photo(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='photo')
    image = models.ImageField(upload_to='shop')


class Address(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='address')

    thana = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
