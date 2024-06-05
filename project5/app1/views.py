from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    output='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>My Projects Links</h1>
    <a href="./Demos/index.html">My Profile Page</a>
    <br><br>
    <a href="./Demos/Tables Demos 2.html">Tables Demo</a><br><br>
    <a href="./Demos/registraitionForm.html">Registration Form</a>
    
    
</body>
</html>'''
    response=HttpResponse(output)
    return response