from django.shortcuts import render
from django.http import HttpResponse
def d2d1(request):
    return render(request,'hello.html')