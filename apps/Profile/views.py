from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from core.utils.mixins import HeaderMixin, ProfileCellMixin
from core.utils.upload_image import upload_image
from core.utils.get_unique_slug import get_unique_index

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
            for i in range(len(json_groups_info)):
                group = Group.objects.get(index=json_groups_info[i]["index"])
                json_groups_info[i]['students'] = list(student.user.username for student in group.students.all())
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
        user = request.user
        if user.role == 'teacher':
            teacher = Teacher.objects.get(user__id=user.id)
        if 'first_name' in request.POST:
            update_form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            new_profile_picture = request.FILES or None
            if (new_profile_picture and update_form.is_valid()):
                    update_form.cleaned_data["profile_picture"] = upload_image(
                        new_profile_picture["profile_picture"], user.id
                    )
            try:
                if update_form.is_valid():
                    update_form.save(user.username)
                messages.success(request, "Данные сохранены")
                return redirect("profile")
            except:
                messages.error(request, "Неверные данные")
                return redirect("profile")

        elif 'register' in request.POST:
            if user.role != 'teacher':
                messages.error(request, 'Доступ запрещен')
                return redirect('profile')
            
            try:
                group = Group.objects.create(
                    groupname = request.POST['groupname'],
                    teacher = teacher,
                    index = 'group-' + get_unique_index(Group, request.POST['groupname']),
                )
                teacher.groups.add(group)

                for student in request.POST.getlist('students-login'):
                    if not student:
                        continue
                    student = Student.objects.get(user__username = student)
                    group.students.add(student)

                messages.success(request, 'Группа успешно добавлена')
                return redirect('profile')
            
            except:
                messages.error(request, 'Ошибка добавления группы')
                return redirect('profile')
        
        elif 'index' in request.POST:
            if user.role != 'teacher':
                messages.error(request, 'Доступ запрещен')
                return redirect('profile')
            
            try:
                group = Group.objects.get(index = request.POST['index'])
                group.groupname = request.POST['groupname']
                group.students.clear()

                for student in request.POST.getlist('students-login'):
                    if not student:
                        continue
                    student = Student.objects.get(user__username=student)
                    group.students.add(student)
                group.save()
                
                messages.success(request, 'Группа успешно изменена')
                return redirect('profile')
            
            except:
                messages.error(request, 'Ошибка изменения группы')
                return redirect('profile')
    
def delete_group(request, group_index):
     Group.objects.get(index=group_index).delete()
     return redirect('profile')