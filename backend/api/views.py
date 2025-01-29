from .utiles import home_page_render_get, create_book, get_single_book, get_single_book_delete, get_single_book_updatad
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def home_page(request):
    if request.method == 'GET':
        return  home_page_render_get(request)
    if request.method == 'POST':
        return create_book(request)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def getBookNote(request, pk):
    if request.method == 'GET':
        return  get_single_book(request, pk)
    if request.method == 'PUT':
        return  get_single_book_updatad(request, pk)
    if request.method == 'DELETE':
        return  get_single_book_delete(request, pk)
