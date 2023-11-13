from django.urls import path
from . import views

urlpatterns = [path('', views.home, name="blog-home"), path('about/', views.about, name="blog-about"), ]


""" view.home has not '/' string since it is the home page of the blog, about is a further extension of the blog 
    and therefore has a new link extension string """
