from django.urls import path
from . import views

urlpatterns = [
    path('eduBlog', views.blog , name='blog' )
]