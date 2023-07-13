from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Student, Author, Teacher

from .forms import SigninForm, SignupForm

from core.utils.get_current_redirect_name import get_current_redirect_name


def user_auth(request):
    current_user = request.user

    if current_user.is_authenticated:
        return redirect(get_current_redirect_name(current_user))

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

                    return redirect(get_current_redirect_name(user))

                except:
                    messages.error(request, "Неверный логин или пароль")

                    return redirect("auth")

            messages.error(request, "Некорректный ввод полей")

        else:
            if signup_form.is_valid():
                role = signup_form.cleaned_data["role"]

                try:
                    user = signup_form.save()
                    login(request, user)

                    if role == "student":
                        Student.objects.create(user=user)
                    elif role == "author":
                        Author.objects.create(user=user)
                    else:
                        Teacher.objects.create(user=user)

                    messages.success(request, "Успешная регистрация")

                    return redirect(get_current_redirect_name(user))
                except:
                    messages.error(request, "Ошибка регистрации")

                    return redirect("auth")

            messages.error(request, "Некорректный ввод полей")

    return render(request, "auth/AuthPage.html", data)


def user_logout(request):
    current_user = request.user

    if current_user.is_authenticated:
        logout(request)

    return redirect("auth")
