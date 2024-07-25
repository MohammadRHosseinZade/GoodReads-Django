from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, BooksByGenreView, RecommendedBooksView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('by-genre/', BooksByGenreView.as_view(), name='books-by-genre'),
    path('recommendations/', RecommendedBooksView.as_view(), name='recommended-books'),
]
