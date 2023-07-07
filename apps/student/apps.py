from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
<<<<<<< HEAD:apps/author/apps.py
    name = 'author'
    label = 'authorApp'
=======
    name = 'student'
    label = name + 'App'
>>>>>>> task#student:apps/student/apps.py
