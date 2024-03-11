from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from django.shortcuts import get_object_or_404
from .serializers import SongSerializer
from albums.models import Album


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        album = get_object_or_404(Album, pk=album_id)
        serializer.save(album=album)
