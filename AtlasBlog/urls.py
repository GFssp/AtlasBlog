from django.contrib import admin
from django.urls import path
from post.views import (
    homepage_view, 
    about_view, 
    post_detail_view, 
    post_create_view,
    dynamic_lookup_view,
    post_delete_view,
    post_list_view
    )

urlpatterns = [
    path('home/', homepage_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('post/', post_detail_view, name='post'),
    path('create/', post_create_view, name='create'),
    path('posts/<int:id>/', dynamic_lookup_view, name='post-detail'),
    path('posts/<int:my_id>/delete/', post_delete_view, name='delete'),
    path('post_list', post_list_view, name='post_list')
]
