from django.urls import path
from . import views
from . import template_views

urlpatterns = [
    path('about/', template_views.AboutViews.as_view()),
    path('home/', template_views.HomePageViews.as_view()),
    path('contact/', template_views.ContactViews.as_view()),

    path('profile/', views.index, name='profile'),
    path('profile/edit/', views.Index_2.as_view(), name='profile_edit'),
]