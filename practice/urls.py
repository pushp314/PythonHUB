from django.urls import path
from .views import *

urlpatterns = [
    path('', practice, name='practice')
]
