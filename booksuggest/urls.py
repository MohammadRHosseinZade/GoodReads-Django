from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from django.urls import path, include


urlpatterns = [
    path('auth/', include("Account.urls")),
    path('books/', include("Book.urls")),
    path('reviews/', include("Review.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]