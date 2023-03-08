from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, RawPostForm

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

def post_create_view(request):
    my_form = RawPostForm()
    if request.method == "POST":
        my_form = RawPostForm(request.POST)
        if my_form.is_valid():
            Post.objects.create(**my_form.cleaned_data)
    
    context = {
      "form": my_form
    }
    return render(request, "post_create.html", context)