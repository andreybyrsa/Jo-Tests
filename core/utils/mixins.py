# InfoSidebarMixin
# icons:
# view: bi bi-eye
# change: bi bi-pencil-square
# delete: bi bi-trash3
# colors:
# pirmary
# danger
# success

# HeaderMixin
# create: 'bi bi-plus'
# list: 'bi bi-list'
# profile: 'bi bi-person-gear'

header = [
    {"name": "Список тестов", "url_name": "tests", "icon_name": "bi bi-list"},
    {
        "name": "Создать тест",
        "url_name": "create_test",
        "icon_name": "bi bi-file-earmark-plus",
    },
    {"name": "Список курсов", "url_name": "courses", "icon_name": "bi bi-list"},
    {
        "name": "Создать курс",
        "url_name": "create-course",
        "icon_name": "bi bi-file-earmark-plus",
    },
    {"name": "Профиль", "url_name": "profile", "icon_name": "bi bi-person"},
]

info_course_student = [
    {
        "name": "Посмотреть курс",
        "url_name": "inspect-test",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
]

info_course_teacher = [
    {
        "name": "Посмотреть курс",
        "url_name": "inspect-course",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
    {
        "name": "Редактировать курс",
        "url_name": "change-course",
        "icon_name": "bi bi-pencil-square",
        "color": "primary",
    },
    {
        "name": "Удалить курс",
        "url_name": "delete-course",
        "icon_name": "bi bi-trash3",
        "color": "danger",
    },
]

info_test_teacher = [
    {
        "name": "Посмотреть тест",
        "url_name": "inspect-course",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
]

info_test_author = [
    {
        "name": "Редактировать тест",
        "url_name": "change-test",
        "icon_name": "bi bi-pencil-square",
        "color": "primary",
    },
    {
        "name": "Удалить тест",
        "url_name": "delete-test",
        "icon_name": "bi bi-trash",
        "color": "danger",
    },
]


class InfoSidebarMixin:
    def get_user_sidebar(self, location="course"):
        context = {}
        current_user = self.request.user
        if current_user.role == "teacher":
            context["info"] = info_course_teacher
            if location != "course":
                context["info"] = info_test_teacher
        elif current_user.role == "student":
            context["info"] = info_course_student
        else:
            context["info"] = info_test_author
        return context


class HeaderMixin:
    def get_user_header(self):
        context = {}
        current_user = self.request.user
        user_header = header.copy()
        if current_user.role == "author":
            user_header.pop(3)
            user_header.pop(2)
        elif current_user.role == "teacher":
            user_header.pop(1)
        else:
            user_header.pop(3)
            user_header.pop(1)
            user_header.pop(0)
        context["header"] = user_header
        return context
