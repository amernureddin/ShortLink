from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    re_path(r'^(?P<id>\w+)$', views.link)
]
