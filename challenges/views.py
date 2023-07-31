from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def january(request):
    return HttpResponse("一周運動兩次")

def february(request):
    return HttpResponse("一個月不喝含糖飲料")


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "一周運動兩次"
    elif month == "february":
        challenge_text = "一個月不喝含糖飲料"
    else:
        return HttpResponseNotFound("尚不支援輸入的月份")

    return HttpResponse(challenge_text)