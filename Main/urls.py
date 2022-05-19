from django.urls import path, include
from .views import Index, AddContact

urlpatterns = [
    path('', Index, name='index'),
    path('add-contact/', AddContact , name='add-contact'), 

]