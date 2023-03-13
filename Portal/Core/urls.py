from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.login_page, name="login_page"),
]