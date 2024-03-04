from django import forms
from film.models import genre,movie

class GenreForm(forms.ModelForm):
    class Meta:
        model=genre
        fields="__all__"

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields="__all__"