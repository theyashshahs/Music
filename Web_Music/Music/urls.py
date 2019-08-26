from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   url(r'^$', views.index , name = 'index'),
   
   url(r'^(?P<album_id>[0-9]+)/', views.details, name = 'details'),     
]

#urlpatterns = [
#    path('', views.index, name = 'index'),
#     #music/grouping-objects
#    path('(?P<album_id>[0-9]+)/', views.details, name = 'details'),    

#]

