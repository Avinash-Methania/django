from django.shortcuts import render

# Create your views here.
def test_view(request):
    a=10
    b=20
    c=a+b
    c={'a':a,'b':b,'c':c}
    return render(request,'app1/index.html',context=c)