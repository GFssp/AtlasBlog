from django.shortcuts import render, get_object_or_404, redirect
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
    initial_data = {
        'title': "Blog Title" 
    }
    my_form = RawPostForm()
    obj = Post.objects.get(id=1)
    if request.method == "POST":
        my_form = RawPostForm(request.POST or None, instance=obj)
        if my_form.is_valid():
            Post.objects.create(**my_form.cleaned_data)
            my_form.save()
    
    context = {
      "form": my_form
    }
    return render(request, "post_create.html", context)

def dynamic_lookup_view(request, id):
    obj = Post.objects.get(id=id)
    obj = get_object_or_404(Post, id=id)
    context = {
        "object": obj
    }
    return render(request, "post_detail.html", context)

def post_delete_view(request, my_id):
    obj = get_object_or_404(Post, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, "post_delete_view.html", context)

def post_list_view(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "post_list.html", context)