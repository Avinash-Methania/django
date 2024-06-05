from django.shortcuts import render

# Create your views here.

def test_view(request):
    stud_data={'rollno':101,'name':'naresh','course':'python'}
    c={"stud":stud_data}
    return render(request,'app1/index.html',context=c)