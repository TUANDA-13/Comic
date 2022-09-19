from django.urls import path,include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', ViewedComic.as_view() ,name='history'),
    path('<int:page>', ViewedComic.as_view() ,name='history'),
]