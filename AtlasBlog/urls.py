from django.contrib import admin
from django.urls import path
from post.views import homepage_view

urlpatterns = [
    path('home/', homepage_view, name='home/'),
    path('admin/', admin.site.urls),
]
