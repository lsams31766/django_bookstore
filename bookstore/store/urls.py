'''
Created on Feb 23, 2019

@author: lawrencesamuels
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)',views.book_details, name='book_details'),
    url(r'^add/(\d+)',views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)',views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/',views.cart, name='cart'),        
]