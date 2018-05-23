from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from listing.models import Movies
from django.shortcuts import render,get_object_or_404

import api.serializers as serializers

class MoviesListAPIView(APIView):
    def get(self,request):
        queryset = get_object_or_404(Movies,pk=1)
        #queryset = Movies.get_listing(Movies)
        serializer_class = serializers.MovieListSerializer(queryset)
        return Response(serializer_class.data)



