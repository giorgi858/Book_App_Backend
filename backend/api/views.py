from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .serializers import  Books_noteSerializer
from .models import Books_Note
from django.contrib.auth.models import User
from .serializers import UserSerializer

# class BookListAPIView(generics.ListAPIView):
#     queryset = Books_Note.objects.all()
#     serializer_class = Books_noteSerializer
#     parser_classes = [IsAuthenticated]

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books_Note.objects.all().order_by('-updated')
    serializer_class = Books_noteSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Books_Note.objects.all()
    serializer_class = Books_noteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Books_Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    

# class BookDelete(generics.DestroyAPIView):
#     serializer_class = Books_noteSerializer
#     permission_classes = [IsAuthenticated]  
    
#     def get_queryset(self):
#         user = self.request.user
#         return Books_Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  
