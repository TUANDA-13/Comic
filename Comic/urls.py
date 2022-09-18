from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    path('test/', Test ,name='test'),
    path('<int:id>',ComicInfo.as_view(),name='comic'),
    path('category/<int:id>',CategoryView.as_view(),name='category'),
    path('<int:id>/<int:id_chap>',ChapterView.as_view(),name='chapter'),
    # path('add-comment', AddComment,name="add-comment")
]