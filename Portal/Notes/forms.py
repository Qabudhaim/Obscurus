from django import forms
from taggit.forms import TagField
from Notes.models import Note, Reference
from urllib.parse import urlparse
from django.core.exceptions import ValidationError
import validators
from PIL import Image
from io import BytesIO
import requests

class NoteForm(forms.ModelForm):
    tags = TagField(required=False)
    references = forms.CharField(required=False)
    cover = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean_references(self):
        """
        Split the input value into a list of references and validate each reference.
        """
        references = self.cleaned_data.get('references')

        if references:
            references = references.replace(" ", "")
            references = references.split(',')
            if '' in references:
                references.remove('')

            for url in references:
                if validators.url(url):
                    pass
                else:
                    raise ValidationError(f"'{url}' is not a valid URL.")

        return references
    
    def clean_cover(self):
        cover = self.cleaned_data.get('cover')
        if cover:
            if validators.url(cover):
                try:
                    response = requests.get(cover)
                    img = Image.open(BytesIO(response.content))
                    img.close()
                except:
                    raise ValidationError("The URL is not a valid image.")
                pass
            else:
                raise ValidationError(f"'{cover}' is not a valid URL.")
        return cover
    
    def clean_tags(self):
        tags = self.request.POST.getlist('tags')
        return tags

    class Meta:
        model = Note
        fields = ['title', 'cover', 'tags', 'references', 'description', 'body']