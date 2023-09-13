from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.index, name='profile'),
    path('profile/edit/', views.Index_2.index, name='profile_edit'),
]