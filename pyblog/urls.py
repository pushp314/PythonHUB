from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog_detail/', blogDetail, name='blogDetail')
]
