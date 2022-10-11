from django import forms
from .models import Song
#from urllib import request
#from django.core.files.base import ContentFile
#from django.utils.text import slugify

class SearchForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'query', 'album', 'songId', 'preview', 'uri', 'mainArtist', 'image')
        widgets = {
            'title': forms.HiddenInput, 
            'query': forms.HiddenInput, 
            'album': forms.HiddenInput, 
            'songId': forms.HiddenInput, 
            'preview': forms.HiddenInput, 
            'uri': forms.HiddenInput, 
            'mainArtist': forms.HiddenInput, 
            'image': forms.HiddenInput
        }

    # def save(self, force_insert=False, force_update=False, commit=True):
    #     query = super().save(commit=False)
        # image_url = self.cleaned_data['url']
        # name = slugify(image.title)
        # extension = image_url.rsplit('.', 1)[1].lower()
        # image_name = f'{name}.{extension}'

        # download image from the given URL
        # response = request.urlopen(image_url)
        # image.image.save(image_name,
        #                  ContentFile(response.read()),
        #                  save=False)
        # if commit:
        #     image.save()
        # return image

class SearchForm(forms.Form):
	item = forms.CharField(required = True, label = 'Item', max_length = 100
		)