from django.urls import path
from .views import *

app_name = 'forum'  

urlpatterns = [
    path('', forum, name='forum'),
    path('category/<int:id>/', category_posts, name='category_posts'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
]
