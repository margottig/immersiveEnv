from django.urls import path
from . import views

app_name = 'tracks_app'

urlpatterns = [
    path('search/', views.search, name='search')
]