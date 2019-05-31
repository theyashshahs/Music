from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/Music/' + str(album.id) + '/'
        html += '<a href = " ' + url +  '" > ' + album.album_title + ' </a><br> '

    return HttpResponse(html)

def details(request,album_id):
    return HttpResponse('<h2> Details for Album id : ' + str(album_id) + '</h2>')