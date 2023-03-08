from django.contrib import admin
from django.urls import path
from post.views import homepage_view, about_view, post_detail_view

urlpatterns = [
    path('home/', homepage_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('post/', post_detail_view, name='post')
]
