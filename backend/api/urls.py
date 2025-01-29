from django.urls import path
from .views import home_page, getBookNote

urlpatterns = [
    path('', home_page, name='home'),
    path('<str:pk>', getBookNote , name='route')
    
    
]