from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def login(request):
    if request.user.is_authenticated:
        return redirect("pages:home")

    if request.POST:
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login_user(request, user)
            return redirect("pages:home")
        else:
            messages.error(request, "登入失敗，請重新登入一次。")
            return redirect("users:login")
    return render(request, "users/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("pages:home")

    if request.POST:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "兩次密碼輸入不一致！")
            return redirect("users:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, f"使用者 {username} 已被註冊！")
            return redirect("users:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, f"信箱 {email} 已被註冊！")
            return redirect("users:register")

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "註冊成功!歡迎登入。")
        return redirect("users:login")
    return render(request, "users/register.html")


@login_required
def logout(request):
    logout_user(request)
    messages.success(request, "已登出")
    return redirect("pages:home")
