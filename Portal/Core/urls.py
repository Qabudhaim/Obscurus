from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]