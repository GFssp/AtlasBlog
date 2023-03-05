from django.shortcuts import render
from django.http import HttpResponse

# This project uses Functions Based View
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>Welcome!</h1>")