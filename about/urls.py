from django.urls import path
from . import views  # <-- Make sure this dot (.) is there!

urlpatterns = [
    path('', views.about_me, name='about'),
]