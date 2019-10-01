from django.shortcuts import render,get_object_or_404
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):

    album = get_object_or_404(Album, pk = album_id)  #replaces entire try and catch

    return render(request, 'music/details.html', {'album':album})  # another way of doing the dictionary work

def favourite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
            return render(request, 'music/details.html', {
            'album':album,
            'error_message':"You did not selecct a valid song",
            })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album':album}) # adds songs to favourite list