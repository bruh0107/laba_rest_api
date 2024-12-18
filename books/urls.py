from django.urls import path
from .views import BookListCreateAPIView, AuthorListCreateAPIView, BookDetailView, AuthorDetailView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail')
]
