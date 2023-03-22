from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Post


class NewForm(forms.Form):
    t = forms.CharField(label="search")


def index(request):
    return HttpResponse("MEga ЖОПА")


def blog_page(request, post_slug):
    s = post_slug
    return render(request, "blog_page.html", {"form": NewForm})


def main_page(request):
    post_from_admin = Post.objects.all()
    return render(request, "index.html", {"form": NewForm, "posts": post_from_admin})
