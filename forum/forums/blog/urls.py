from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns =[
    path('',views.index,name='forum-home'),
    path('create_thought',views.create_thought, name='create-thought'),
    path('delete_thoughts',views.delete_thought, name='delete-thoughts'),
    path('random_thoughts',views.random,name='random-thoughts'),
    path('like_thoughts',views.like_thought,name='like-thought'),
    path('dislike_thoughts',views.dislike_thought,name='dislike-thought')
]