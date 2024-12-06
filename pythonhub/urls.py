from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pyblog.urls')),
    path('admin/', admin.site.urls),
    path('practice/', include('practice.urls')),
    path('forum/', include('pyforum.urls', namespace='forum')),  # namespace 'forum'
    path('auth/', include('accounts.urls')),

]
