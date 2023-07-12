# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from core.utils.mixins import HeaderMixin, ProfileCellMixin
from .forms import UpdateProfileForm


class UserProfileView(LoginRequiredMixin, HeaderMixin, ProfileCellMixin, View):
    login_url = "/auth/"
    redirect_field_name = "next"

    def get(self, request):
        user = request.user

        form = UpdateProfileForm(instance=user)
        header_def = self.get_user_header()
        cells_def = self.get_profile_cell()
        context = dict(
            list({"user": user, "form": form}.items())
            + list(header_def.items())
            + list(cells_def.items())
        )
        return render(request, "Profile/ProfilePage.html", context)

    def post(self, request):
        user = request.user
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        try:
            form.save()
            messages.success(request, "Данные сохранены")
            redirect("profile")
        except:
            messages.error(request, "Неверные данные")
            redirect("profile")
        header_def = self.get_user_header()
        cells_def = self.get_profile_cell()
        context = dict(
            list({"user": user, "form": form}.items())
            + list(header_def.items())
            + list(cells_def.items())
        )
        return render(request, "Profile/ProfilePage.html", context)
