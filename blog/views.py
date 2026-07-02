# blog/views.py
from django.shortcuts import render
# 1. Add the HttpResponse import
from django.http import HttpResponse

# 2. Add the function to return the text string
def blog_index(request):
    return HttpResponse("Hello, blog!")
