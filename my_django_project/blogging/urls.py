from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("post_comment",views.post_comment,name="post_comment"),
    path("",views.blog_home, name="blog_home"),
    path("<str:slug>",views.blog_post, name="blog_post")
]
