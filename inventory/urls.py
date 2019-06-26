from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display-laptop/', views.display_laptops, name='display-laptop'),
    path('display-desktop/', views.display_desktops, name='display-desktop'),
    path('display-mobile/', views.display_mobiles, name='display-mobile'),

    path('add-laptop/', views.add_laptop, name='add-laptop'),
    path('add-desktop/', views.add_desktop, name='add-desktop'),
    path('add-mobile/', views.add_mobile, name='add-mobile'),

    path('edit-laptop/<int:pk>/', views.edit_laptop, name='edit-laptop'),
    path('edit-desktop/<int:pk>/', views.edit_desktop, name='edit-desktop'),
    path('edit-mobile/<int:pk>/', views.edit_mobile, name='edit-mobile'),

    path('delete-laptop/<int:pk>/', views.delete_laptop, name='delete-laptop'),
    path('delete-desktop/<int:pk>/', views.delete_desktop, name='delete-desktop'),
    path('delete-mobile/<int:pk>/', views.delete_mobile, name='delete-mobile'),
]