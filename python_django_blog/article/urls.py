from django.urls import path

from python_django_blog.article import views

urlpatterns = [
    path("", views.index),
]