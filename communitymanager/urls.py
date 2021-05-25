from django.urls import path
from . import views


urlpatterns = [
    path('communautes/', views.communautes, name='communautes'),
    path('communaute/<int:id>', views.communaute, name="communaute"),
    path('post/<int:id>', views.post, name="post"),
    path('nouveau_post', views.nouveau_post, name='nouveau_post'),
    path('modif_post/<int:id>', views.modif_post, name='modif_post'),
    path('news_feed/', views.news_feed, name='news_feed'),
]