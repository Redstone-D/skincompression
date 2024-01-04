from django.urls import path 

from . import views 

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("process/<int:rid>", views.process, name="process"), 
    path("app/<int:rid>", views.app, name="app"), 
    path("picture/<int:rid>/<int:pid>", views.picture, name="picture"), 
    path("getcompress/<int:rid>", views.getcompress, name="getcompress") 
] 
