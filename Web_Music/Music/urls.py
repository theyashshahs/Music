from django.conf.urls import url
from django.urls import path
from Music import views

app_name = 'music'

urlpatterns = [
   url(r'^$', views.index , name='index'),  # landing page
   url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),     # details of the songs
   url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),  # favourite function
]
