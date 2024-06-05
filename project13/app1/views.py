from django.shortcuts import render

# Create your views here.

def test_view(request):
    courses_list=["PYTHON","JAVA",".NET","DJANGO","ORACLE","AVINASH"]
    c={'list1':courses_list}
    return render(request,'app1/index.html',context=c)