from django.urls import path
from .views import home_page, getBookNote

urlpatterns = [
    path('books/', home_page, name='home'),
    path('books/<str:pk>/', getBookNote , name='route')
    
    
]