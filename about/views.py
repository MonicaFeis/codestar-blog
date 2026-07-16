from django.shortcuts import render
from .models import About  # <-- Make sure you imported the model!

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {"about": about},
    )