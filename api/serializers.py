from django.forms import widgets
from rest_framework import serializers
from listing.models import Movies


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields='__all__'
