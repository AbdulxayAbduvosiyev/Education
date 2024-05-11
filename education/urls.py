from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index' ),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about , name='about' ),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers , name='teachers'),
]
