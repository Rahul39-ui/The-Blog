
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update")
    
]
