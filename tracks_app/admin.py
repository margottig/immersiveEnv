from django.contrib import admin
from .models import Song, SongReview

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'query', 'album', 'songId', 'preview', 'uri', 'mainArtist', 'image']
    list_filter = ['songId']

@admin.register(SongReview)
class SongReviewAdmin(admin.ModelAdmin):
    list_display = ['songId', 'albumId', 'songTitle', 'albumTitle', 'rating', 'comment', 'image']
    list_filter = ['songId']

# Register your models here.
