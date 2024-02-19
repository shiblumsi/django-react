from django.urls import path
from .views import ShopCreateView,AddressView
urlpatterns = [
    path('sc', ShopCreateView.as_view(), name='shop-create'),
    path('ac', AddressView.as_view(), name='address-create'),
]