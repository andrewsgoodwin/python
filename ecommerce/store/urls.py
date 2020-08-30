from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url('admin', admin.site.urls),
    url('cart', views.cart, name="cart"),
    url('checkout', views.checkout, name="checkout"),
    url('', views.store, name="store"),
]
