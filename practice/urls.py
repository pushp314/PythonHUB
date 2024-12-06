# compiler/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', compiler_page, name='practice'),
    path('run_code/', run_code, name='run_code'),
    path('optimize_code/', optimize_code, name='optimize_code'),
]
