# from django.utils.text import slugify
from django.db import models
from django.conf import settings

# class Track(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tracks_added', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, blank=True)
#     image = models.ImageField(upload_to='images/%Y/%m/%d/')
#     description = models.TextField(blank=True)
#     created_at = models.DateField(auto_now_add=True, db_index=True)
#     users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)


class Song(models.Model):
	title = models.CharField(max_length=100, default='No song title')
	query = models.CharField(max_length=100, default='No query')
	album = models.CharField(max_length=100, default='No album')
	songId = models.CharField(max_length=100, primary_key=True)
	preview = models.CharField(max_length=400, default='None', blank=True, null=True)
	external = models.CharField(max_length=100, default='No external URL')
	uri = models.CharField(max_length=100, default='No URI')
	duration = models.CharField(max_length=10, default='No duration')
	mainArtist = models.CharField(max_length=100, default='No artist')
	artists = models.CharField(max_length=100, default='No artists')
	popularity = models.FloatField(max_length=101, default=0)
	image = models.CharField(max_length=200, default='None', null=True, blank=True)
	theType = models.CharField(max_length = 10, default='No type')
	albumId = models.CharField(max_length=100, default='None')
	artistId = models.CharField(max_length=100, default='None')


class SongReview(models.Model):
	songId = models.CharField(max_length=100, default='No song', null=True, blank=True)
	albumId = models.CharField(max_length=100, default='No album', null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='songs_reviewed', on_delete=models.CASCADE)
	comment = models.CharField(max_length = 500, default='No comment')
	songTitle = models.CharField(max_length=500, default='No song title', null=True, blank=True)
	albumTitle = models.CharField(max_length=500, default='No album title', null=True, blank=True)
	songArtists = models.CharField(max_length=500, default='No artists', null=True, blank=True)
	rating = models.FloatField(max_length=10, default=1)
	time = models.CharField(max_length=50, default='No date')
	image = models.CharField(max_length=500, default='No image')