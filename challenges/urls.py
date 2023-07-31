from django.urls import path
from . import views

urlpatterns = [
    # path('january', views.january),
    # path('february', views.february),
    # 可以用這種<>的方式，將<>中的參數傳給 views的函式，但是那裏需要有同名的參數才行！
    path('<month>', views.monthly_challenges)
]