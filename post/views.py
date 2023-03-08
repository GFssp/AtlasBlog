from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# This project uses Functions Based View
def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    context = {
        "my_text": "This is about us",
        "code": 202,
        "my_list": [254, 234]
    }
    return render(request, "about.html", context)

def post_detail_view(request):
    obj = Post.objects.get(id=1)
    context = {
        'title': obj.title,
        'subtitle': obj.subtitle,
        'text': obj.text,
    }
    return render(request, "posts.html", context)