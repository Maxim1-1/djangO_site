from django.shortcuts import render
from django.http import HttpResponse
from django import forms


class NewForm(forms.Form):
    t = forms.CharField(label="search")


def index(request):
    return HttpResponse("MEga ЖОПА")


def blog_page(request):
    return render(request, "blog_page.html", {"form": NewForm})


def main_page(request):
    return render(request, "index.html", {"form": NewForm})
