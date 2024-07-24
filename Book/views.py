from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Genre, GenreBook
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksByGenreView(APIView):
    def get(self, request):
        genre_name = request.query_params.get('genre')
        if not genre_name:
            return Response({'error': 'Genre parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            genre = Genre.objects.get(name=genre_name)
        except Genre.DoesNotExist:
            return Response({'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)
        
        genre_books = GenreBook.objects.filter(genre=genre)
        books = [genre_book.book for genre_book in genre_books]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)