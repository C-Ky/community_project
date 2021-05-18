from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage_user, name='homepage_user'),
]