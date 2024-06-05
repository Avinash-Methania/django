from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def add(request,a,b):
    c=a+b
    d=f'<h1> Addition of {a} and {b} = {c}</h1>'
    response=HttpResponse(d)
    return response

def otp_view(request,name):
    otp=random.randint(100000,999999)
    output=f'<h1> {name} Your OTP Is {otp}</h1>'
    response=HttpResponse(output)
    return response