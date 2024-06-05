from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    msg=["<h1> Hello Avinash Methania ji </h1><br>","<h2>Hello Garima</h2>"]
    return HttpResponse(msg)
