from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("一周運動兩次")

def february(request):
    return HttpResponse("一個月不喝含糖飲料")