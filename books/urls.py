from django.urls import path
from .views import BookListCreateAPIView, AuthorListCreateAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
]
