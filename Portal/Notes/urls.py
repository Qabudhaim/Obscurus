from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Notes'

urlpatterns = [
    path('', views.index, name="index"),
    path('personal_area/', views.personal_area, name="personal_area"),
    path('add_note/', views.add_note, name="add_note"),
    path('show_note/<int:id>', views.show_note, name="show_note"),
    path('delete_note/<int:id>', views.delete_note, name="delete_note"),
    path('update_note/<int:id>', views.update_note, name="update_note"),
    path('export_note/<int:id>', views.export_note, name="export_note"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
