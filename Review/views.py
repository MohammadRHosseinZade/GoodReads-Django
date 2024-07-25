from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    get=extend_schema(
        responses={200: ReviewSerializer(many=True)},
        description="Retrieve a list of reviews for the current user"
    ),
    post=extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
        description="Create a new review for the current user"
    )
)
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    get=extend_schema(
        responses={200: ReviewSerializer},
        description="Retrieve a specific review by ID for the current user"
    ),
    put=extend_schema(
        request=ReviewSerializer,
        responses={200: ReviewSerializer},
        description="Update a specific review by ID for the current user"
    ),
    patch=extend_schema(
        request=ReviewSerializer,
        responses={200: ReviewSerializer},
        description="Partially update a specific review by ID for the current user"
    ),
    delete=extend_schema(
        responses={204: None},
        description="Delete a specific review by ID for the current user"
    )
)
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)