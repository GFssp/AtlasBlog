from django.shortcuts import render
from django.http import HttpResponse

# This project uses Functions Based View
def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})