from django.shortcuts import render
from django.http import HttpResponse

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
