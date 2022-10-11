from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Song
from .api_credentials import CLIENT_ID, CLIENT_SECRET

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



credentials = SpotifyClientCredentials(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET)


@login_required
def search(request):
	sp = spotipy.Spotify(auth_manager=credentials)
	musicData = 'there is an error'
	if request.GET:
		searchname = request.GET.get('q')
		if 'r' in request.GET:
			Song.objects.all().delete()
			try:
				results = sp.search(q=searchname, limit=50, type='track')
				for i,t in enumerate(results['tracks']['items']):
					theTitle = t['name']
					theAlbum = t['album']['name']
					albumId = t['album']['id']
					theId = t['id']
					theType=t['type']
					thePreview = t['preview_url']
					theExternal = t['external_urls']['spotify']
					theURI = t['uri']
					theMainArtist = t['artists'][0]['name']
					somelist = [x['name'] for x in t['artists']]
					theArtists = ', '.join(somelist)
					thePopularity = float(t['popularity'])
					thatList = [str(x) for x in t['available_markets']]
					theMarkets = ', '.join(thatList)
					artistId = t['artists'][0]['id']
					if not t['album']['images']:
						theImage = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
					else:
						theImage = t['album']['images'][0]['url']
					theSong = Song.objects.create(title=theTitle,theType=theType,query=searchname,albumId=albumId,album=theAlbum,songId=theId,preview=thePreview,external=theExternal,uri=theURI,duration='none',mainArtist=theMainArtist,artists=theArtists,popularity=thePopularity,image=theImage,artistId=artistId)
					musicData = Song.objects.filter(query=searchname)
			except:
				musicData = "there is a song error"
		return render(request, 'search.html',{'musicData': musicData, 'search': True})
	else:
		return render(request, 'search.html') 



# Create your views here.
