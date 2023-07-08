from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SigninForm, SignupForm


def user_auth(request):
    current_user = request.user

    if current_user.is_authenticated:
        return redirect("tests")  # поменяете на нужный url

    signin_form = SigninForm(request.POST or None)
    signup_form = SignupForm(request.POST or None)
    data = {"signin_form": signin_form, "signup_form": signup_form}

    if request.method == "POST":
        if "login" in request.POST:
            if signin_form.is_valid():
                username = signin_form.cleaned_data["username"]
                password = signin_form.cleaned_data["password"]

                try:
                    user = authenticate(request, username=username, password=password)
                    login(request, user)
                    messages.success(request, "Успешный вход в аккаунт")

                    return redirect("tests")  # поменяете на нужный url
                except:
                    messages.error(request, "Неверный логин или пароль")

                    return redirect("auth")

            messages.error(request, "Некорректный ввод полей")

        else:
            if signup_form.is_valid():
                try:
                    user = signup_form.save()
                    login(request, user)
                    messages.success(request, "Успешная регистрация")

                    return redirect("tests")  # поменяете на нужный url
                except:
                    messages.error(request, "Ошибка регистрации")

                    return redirect("auth")

            messages.error(request, "Некорректный ввод полей")

    return render(request, "auth/auth.html", data)


def user_logout(request):
    current_user = request.user

    if current_user.is_authenticated:
        logout(request)

    return redirect("auth")
