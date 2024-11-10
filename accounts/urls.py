from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signin, signup

urlpatterns = [
    path('signup/', signup, name='signup'),  # Custom signup view
    path('login/', signin, name='login'),  # Use the custom signin view
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout view with redirect to home
]
