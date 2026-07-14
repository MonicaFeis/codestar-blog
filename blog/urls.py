# blog/urls.py
from django.urls import path
from . import views  # Make sure your views are imported

urlpatterns = [
    # ⚠️ DO NOT use include("blog.urls") here!
    # Map directly to your views instead:
    path("", views.PostList.as_view(), name="home"), 
]