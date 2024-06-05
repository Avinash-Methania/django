from django.shortcuts import render

# Create your views here.

def test_view(request,a,b):
    c=a+b
    result={'a':a,'b':b,'c':c}
    return render(request,'app1/index.html',context=result)