from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(reuest):
    return HttpResponse('hello home page')