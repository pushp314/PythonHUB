from django.urls import path
from .views import *

urlpatterns = [
    path('', forum, name='forum')
]
