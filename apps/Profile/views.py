# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from core.utils.mixins import HeaderMixin, ProfileCellMixin
from core.utils.upload_image import upload_image
from .forms import UpdateProfileForm, FindGroupStudentForm, GroupEditForm



class UserProfileView(LoginRequiredMixin, HeaderMixin, ProfileCellMixin, View):
    login_url = "/auth/"
    redirect_field_name = "next"

    def get(self, request):
        user = request.user
        find_group_student_form = FindGroupStudentForm()
        group_edit_form = GroupEditForm()
        update_profile_form = UpdateProfileForm(instance=user)
        header_def = self.get_user_header()
        cells_def = self.get_profile_cell()
        context = dict(
            list({"user": user, "update_profile_form": update_profile_form, "find_group_student_form": find_group_student_form, "group_edit_form": group_edit_form}.items())
            + list(header_def.items())
            + list(cells_def.items())
        )
        return render(request, "Profile/ProfilePage.html", context)

    def post(self, request):
        if 'first_name' in request.POST:
            user = request.user
            update_form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            new_profile_picture = request.FILES or None
            if (new_profile_picture):
                    update_form.cleaned_data["profile_picture"] = upload_image(
                        new_profile_picture["profile_picture"], user.id
                    )
            try:
                update_form.save()
                messages.success(request, "Данные сохранены")
                return redirect("profile")
            except:
                messages.error(request, "Неверные данные")
                return redirect("profile")
