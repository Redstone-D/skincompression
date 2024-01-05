from django.urls import path 

from . import views 

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("process/<int:rid>", views.process, name="process"), 
    path("app/<int:rid>", views.app, name="app"), 
    path("app/getprop/<int:pid>", views.getskinprop, name="getskinprop"), 
    path("process/<int:pid>/changename", views.changeName, name="changeName"), 
    path("process/<int:pid>/changemodel", views.changeModel, name="changeModel"), 
    path("picture/<int:pid>", views.picture, name="picture"), 
    path("getcompress/<int:rid>", views.getcompress, name="getcompress") 
] 
