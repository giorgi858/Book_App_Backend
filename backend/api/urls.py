from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='books'),  
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='single-book'),
]   
