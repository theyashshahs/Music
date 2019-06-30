from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):
    try:
        album = Album.objects.get(pk = album_id)
    
    except Album.DoesNotExist : 
        raise Http404("Album does not exist")

    return render(request, 'music/details.html', {'album':album})  #another way of doing the dictionary work