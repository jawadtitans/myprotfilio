from django.shortcuts import render
from django.http import HttpRequest


def home(request):
    return render(request,"index.html");

