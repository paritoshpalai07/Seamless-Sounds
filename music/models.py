from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)  # Optional


    def __str__(self):
        return f"{self.name}"

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.CharField(max_length=100, blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/')  # Stores music files in 'media/songs/'
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)  # Optional
    duration = models.CharField(max_length=20, blank=True)  # e.g., "3:45"
    lyrics = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
    

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"