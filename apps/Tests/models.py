from django.db import models
from apps.auth.models import Student, Author


class Test(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.TextField(max_length=127, verbose_name="Название теста")
    description = models.TextField(max_length=255, verbose_name="Описание")
    count = models.IntegerField(verbose_name="Количество вопросов")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    date_expired = models.DateTimeField(
        auto_now=True, verbose_name="Дата истекания доступа к тесту"
    )
    questions = models.ManyToManyField(
        "TestsApp.Question",
        verbose_name="Вопросы",
        related_name="+",
        blank=True
    )
    test_time = models.TimeField(verbose_name="Длительность теста")
    max_result = models.IntegerField(verbose_name="Максимальный результат")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def get_test_info(self):
        return {
            "title": self.title,
            "description": self.description,
            "time_create": self.time_create,
            "time_update": self.time_update,
            "questions_amount": self.count,
            "test_time": self.test_time,
            "max_result": self.max_result,
        }

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("time_update", "title")
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class StudentResult(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент"
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    result = models.FloatField(verbose_name="Результат")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Результат студента"
        verbose_name_plural = "Результаты студентов"


class Question(models.Model):
    class QuestionType(models.TextChoices):
        SINGLE = "single"
        MULTIPLE = "multiple"

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    question = models.TextField(max_length=255, verbose_name="Вопрос")
    answers = models.ManyToManyField(
        "TestsApp.Answer", related_name="+", verbose_name="Варианты ответа"
    )
    max_points = models.PositiveIntegerField(verbose_name="Максимальное количество баллов")
    qtype = models.CharField(
        max_length=8,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE,
        verbose_name="Тип вопроса",
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос для теста"
        verbose_name_plural = "Вопросы для тестов"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    answer = models.TextField(max_length=255, verbose_name="Вариант ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ для теста"
        verbose_name_plural = "Ответы для тестов"


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент"
    )
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, verbose_name="Ответ"
    )
    is_selected = models.BooleanField(default=False, verbose_name="Выбран")

    class Meta:
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студентов"
