from rest_framework.response import Response
from .models import Books_Note
from .serializers import Books_noteSerializer


def home_page_render_get(request):
    books = Books_Note.objects.all().order_by('-updated')
    serializer = Books_noteSerializer(books, many=True)
    # print('serializer.data', serializer.data)
    return Response(serializer.data)

def create_book(request):
    data = request.data
    book = Books_Note.objects.create(
        content=data['content']
    )
    serializer = Books_noteSerializer(book, many=False)
    return Response(serializer.data)

def get_single_book(request, pk):
    books = Books_Note.objects.get(id=pk)
    serializer = Books_noteSerializer(books, many=False)
    print('serializer.data', serializer.data)
    return Response(serializer.data)

def get_single_book_updatad(request, pk):
    data = request.data
    book = Books_Note.objects.get(id=pk)
    serializer = Books_noteSerializer(instance=book, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def get_single_book_delete(request, pk):
    books = Books_Note.objects.get(id=pk)
    books.delete()
    return Response('book note has benn deleted!')