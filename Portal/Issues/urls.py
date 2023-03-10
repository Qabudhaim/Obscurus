from django.urls import path
from . import views

app_name = 'Issues'

urlpatterns = [
    path('', views.index, name="index")
]