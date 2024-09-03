from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .seriealizers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters 
class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }
    ordering = filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('publication_year', 'publication_year'),
        )
    )

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles listing and creating books with additional functionalities:
    - Filtering by title, author, and publication year.
    - Searching by title and author name.
    - Ordering by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]