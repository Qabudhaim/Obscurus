"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('Core.urls', 'Core'), namespace='Core')),
    path('notes/', include('Notes.urls', namespace='Notes'), name='Notes'),

    path("__reload__/", include("django_browser_reload.urls")),

]

handler404 = 'Core.views.handler404'
handler500 = 'Core.views.handler500'
handler403 = 'Core.views.handler403'
handler400 = 'Core.views.handler400'