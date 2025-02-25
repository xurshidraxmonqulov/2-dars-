from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer