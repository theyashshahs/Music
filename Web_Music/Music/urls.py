from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name = 'index'),
    #music/grouping-objects
    url(r'^(?P<album_id>[0-9]+)$', views.details, name = 'details'),     
]
