from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # home page
    path('create/', views.book_create, name='book_create'),  # add book
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('rules/', views.rules, name='rules'),
    path('contact/', views.contact, name='contact'),
]
