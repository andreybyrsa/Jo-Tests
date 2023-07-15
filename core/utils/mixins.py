header = [
    {
        "name": "Список тестов",
        "url_name": "tests",
        "icon_name": "bi bi-list"
    },
    {
        "name": "Создать тест",
        "url_name": "create-test",
        "icon_name": "bi bi-file-earmark-plus",
    },
    {
        "name": "Список курсов",
        "url_name": "courses",
        "icon_name": "bi bi-list"
    },
    {
        "name": "Создать курс",
        "url_name": "create-course",
        "icon_name": "bi bi-file-earmark-plus",
    },
    {
        "name": "Профиль",
        "url_name": "profile",
        "icon_name": "bi bi-person"
    },
]

profile_cell = [
    {"name": "Настройки профиля"},
    {"name": "Пройденные тесты"},
    {"name": "Добавить группу"},
    {"name": "Список групп"},
]

info_course_student = [
    {
        "name": "Посмотреть курс",
        "url_name": "",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
]

info_course_teacher = [
    {
        "name": "Посмотреть курс",
        "url_name": "",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
    {
        "name": "Редактировать курс",
        "url_name": "change_course/",
        "icon_name": "bi bi-pencil-square",
        "color": "primary",
    },
    {
        "name": "Удалить курс",
        "url_name": "delete_course/",
        "icon_name": "bi bi-trash",
        "color": "danger",
    },
]

info_test_teacher = [
    {
        "name": "Посмотреть тест",
        "url_name": "",
        "icon_name": "bi bi-eye",
        "color": "success",
    },
]

info_test_author = [
    {
        "name": "Редактировать тест",
        "url_name": "change_test/",
        "icon_name": "bi bi-pencil-square",
        "color": "primary",
    },
    {
        "name": "Удалить тест",
        "url_name": "delete_test/",
        "icon_name": "bi bi-trash",
        "color": "danger",
    },
]


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


class ProfileCellMixin:
    def get_profile_cell(self):
        context = {}
        current_user = self.request.user
        user_cells = profile_cell.copy()
        if current_user.role == "author":
            context["cells"] = user_cells[0:1]
        elif current_user.role == "teacher":
            user_cells.pop(1)
            context["cells"] = user_cells
        else:
            context["cells"] = user_cells[0:2]
        return context


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
        elif current_user.role == "author":
            context["info"] = info_test_author
        return context
