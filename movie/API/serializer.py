from rest_framework import serializers
from film.models import movie

class Movie_serializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields="__all__"
        