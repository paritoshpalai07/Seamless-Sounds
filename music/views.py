from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Artist, Playlist
from .forms import PlaylistForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    playlists = Playlist.objects.filter(user=request.user)
    return render(request,'music/index.html', {'songs':songs, 'artists':artists, 'playlists':playlists})

def login(request):
    return render(request, 'music/login.html')

@login_required
def song(request, songID):
    song = Song.objects.get(id=songID)
    otherSongs = Song.objects.exclude(id=songID)
    playlists = Playlist.objects.filter(user=request.user)
    return render(request,'music/song.html', {'song':song, 'otherSongs' : otherSongs, 'playlists':playlists})

def artist_songs(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    songs = Song.objects.filter(artist=artist)
    return render(request, 'music/artist.html', {'artist':artist, 'songs':songs})

def search_songs(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Song.objects.filter(title__icontains=query)

    return render(request, 'music/search_results.html', {'results': results, 'query': query})


@login_required
def create_playlist(request):
    playlists = Playlist.objects.filter(user=request.user)
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()  # For saving many-to-many songs
            return redirect('home')
    else:
        form = PlaylistForm()
    return render(request, 'music/create_playlist.html', {'form': form, 'playlists':playlists})

@login_required
def my_playlists(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'music/my_playlists.html', {'playlists': playlists})

def view_playlist(request, pk):
    playlists = Playlist.objects.filter(user=request.user)
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'music/view_playlist.html', {'playlist': playlist, 'playlists':playlists})