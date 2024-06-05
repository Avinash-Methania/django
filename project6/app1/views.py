from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showdate(request,date):
    output=f'<h1> Today Date Is {date} </h1>'
    return HttpResponse(output)