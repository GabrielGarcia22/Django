from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('login/', views.login_view, name='login_view'),
] 