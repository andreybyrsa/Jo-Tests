# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from core.utils.mixins import HeaderMixin, ProfileCellMixin
from core.utils.upload_image import upload_image
from .forms import UpdateProfileForm, GroupStudentForm
from apps.auth.models import Student, Teacher
from apps.Courses.models import Group




class UserProfileView(LoginRequiredMixin, HeaderMixin, ProfileCellMixin, View):
    login_url = "/auth/"
    redirect_field_name = "next"

    def get(self, request):
        user = request.user
        group_student_form = GroupStudentForm()
        update_profile_form = UpdateProfileForm(instance=user)
        header_def = self.get_user_header()
        cells_def = self.get_profile_cell()
        if user.role == 'teacher':
            students = Student.objects.all()
            teacher = Teacher.objects.get(user__id = user.id)
            teacher_groups = teacher.groups.all()
            json_groups_info = list(group.get_group_info() for group in teacher_groups)
            context = dict(
                list({
                        "user": user,
                        "update_profile_form": update_profile_form,
                        "group_student_form": group_student_form,
                        "students": students,
                        "teacher_groups": teacher_groups,
                        "json_groups_info": json_groups_info,
                    }.items())
                + list(header_def.items())
                + list(cells_def.items())
            )
        elif user.role == 'student':
             student = Student.objects.get(user__id = user.id)
             test_results = student.result_tests.filter(is_passed = True)
             print(test_results)
             context = dict(
                list({
                        "user": user,
                        "update_profile_form": update_profile_form,
                        'test_results': test_results,
                    }.items())
                + list(header_def.items())
                + list(cells_def.items())
            )
        else:
             context = dict(
                list({
                        "user": user,
                        "update_profile_form": update_profile_form,
                    }.items())
                + list(header_def.items())
                + list(cells_def.items())
            )
        
        return render(request, "Profile/ProfilePage.html", context)

    def post(self, request):
        if 'first_name' in request.POST:
            user = request.user
            update_form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            new_profile_picture = request.FILES or None
            if (new_profile_picture and update_form.is_valid()):
                    update_form.cleaned_data["profile_picture"] = upload_image(
                        new_profile_picture["profile_picture"], user.id
                    )
            try:
                update_form.save(user.username)
                messages.success(request, "Данные сохранены")
                return redirect("profile")
            except:
                messages.error(request, "Неверные данные")
                return redirect("profile")

        if 'students-login' in request.POST:
            print(request.POST)      
