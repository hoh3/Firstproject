from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'register',views.register, name='register'),
    url(r'menu',views.products, name='products'),
    url(r'custom_recipe',views.custom, name='custom'),
    url(r'custom_recipe/post', views.custom_post, name='custom_post'),
    url(r'order',views.orders,name='orders'),
    url(r'order/add_to_cart', views.add_to_cart, name='add_to_cart'),
    url(r'cart',views.cart,name='cart'),
]
