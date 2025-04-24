from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login, name='login'),
    path('song/<int:songID>/', views.song, name='song'),
    path('artist/<int:artist_id>/', views.artist_songs, name='artist_songs'),
    path('search/', views.search_songs, name='search_songs'),
    # path('alert/', views.alert, name='alert'),
    path('playlists/', views.my_playlists, name='my_playlists'),
    path('playlists/create/', views.create_playlist, name='create_playlist'),
    path('playlists/<int:pk>/', views.view_playlist, name='view_playlist'),
]