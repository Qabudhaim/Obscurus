from django.urls import path
from . import views

app_name = 'Notes'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_note/', views.add_note, name="add_note"),
    path('show_note/<int:id>', views.show_note, name="show_note"),
    path('delete_note/<int:id>', views.delete_note, name="delete_note"),
    path('update_note/<int:id>', views.update_note, name="update_note"),
]