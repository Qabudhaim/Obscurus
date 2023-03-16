from django import forms
from taggit.forms import TagField
from Notes.models import Note


class NoteForm(forms.ModelForm):
    tags = TagField(required=False)

    class Meta:
        model = Note
        fields = ['title', 'tags', 'description', 'body']