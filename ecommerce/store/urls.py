from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('main_store/', views.main_store, name='main_store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('update_item/', views.updateItem, name="update_item"),

    path('about', views.about, name='about'),
]