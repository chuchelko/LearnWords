from django.urls import path

from . import views

urlpatterns = [
    path('words/', views.all_words_page, name='home'),
    path('', views.index),
]