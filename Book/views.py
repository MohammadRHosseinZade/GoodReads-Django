from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Review.models import Review
from .models import Book, Genre, GenreBook
from .serializers import BookSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema,OpenApiParameter, OpenApiResponse

@extend_schema_view(
    get=extend_schema(
        responses={200: BookSerializer(many=True)},
        description="Retrieve a list of books"
    ),
    post=extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
        description="Create a new book"
    )
)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema_view(
    get=extend_schema(
        responses={200: BookSerializer},
        description="Retrieve a specific book by ID"
    ),
    put=extend_schema(
        request=BookSerializer,
        responses={200: BookSerializer},
        description="Update a specific book by ID"
    ),
    patch=extend_schema(
        request=BookSerializer,
        responses={200: BookSerializer},
        description="Partially update a specific book by ID"
    ),
    delete=extend_schema(
        responses={204: None},
        description="Delete a specific book by ID"
    )
)
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(name='genre', description='Name of the genre', required=True, type=str)
    ],
    responses={
        200: BookSerializer(many=True),
        400: OpenApiResponse(description="Genre parameter is required"),
        404: OpenApiResponse(description="Genre not found"),
    },
    description="Retrieve books by genre"
)
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

@extend_schema(
    responses={200: BookSerializer(many=True)},
    description="Retrieve recommended books based on user reviews"
)
class RecommendedBooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        reviews = Review.objects.filter(user=user, rating__gte=4, rating__lte=5)
        if reviews.count() == 0:
            return Response({"error": "Not enough info"}, status=400)
        reviewed_books = [review.book for review in reviews]
        genre_books = GenreBook.objects.filter(book__in=reviewed_books)
        genres = [genre_book.genre for genre_book in genre_books]
        recommended_books = Book.objects.filter(genrebook__genre__in=genres).exclude(id__in=[book.id for book in reviewed_books]).distinct()
        serializer = BookSerializer(recommended_books, many=True)
        return Response(serializer.data, status=200)
