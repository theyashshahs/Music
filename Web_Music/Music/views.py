from django.shortcuts import render,get_object_or_404
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):
    #try:
    #    album = Album.objects.get(pk = album_id)
    
    #except Album.DoesNotExist : 
    #    raise Http404("Album does not exist")

    album = get_object_or_404(Album, pk = album_id)  #replaces entire try and catch

    return render(request, 'music/details.html', {'album':album})  # another way of doing the dictionary work