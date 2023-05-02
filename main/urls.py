from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_note', views.add_note, name='add_note'),
    path('note/<nid>', views.note, name='note'),
    path('remove/<nid>', views.remove, name='remove'),
    path('edit/<nid>', views.edit, name='edit'),
]