from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer