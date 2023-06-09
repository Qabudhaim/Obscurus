from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user_settings/', views.user_settings, name='user_settings'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('remove_tag/<int:id>', views.remove_tag, name='remove_tag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)