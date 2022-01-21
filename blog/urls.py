from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"), #/blog/postComment
    path('', views.blogHome, name="bloghome"),  #for blog/
    path('<str:slug>', views.blogPost, name="blogPost"), #for blog/some_string
    
    
]

