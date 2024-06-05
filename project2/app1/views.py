from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f1(request):
    return HttpResponse("<h1>Hello Avinash Methania How Are You</h1>")

def f2(request):
    return HttpResponse("<h1>I Am Good What About You</h1>")

def f3(request):
    return HttpResponse("<h1>I Am Also Good</h1>")