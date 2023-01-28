from django.urls import path
from .views import *

urlpatterns = [
    path('blog_page/', blog_page)
]
