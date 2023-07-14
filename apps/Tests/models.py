from django.db import models
from django.urls import reverse
from apps.auth.models import Student, Author


class Test(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.TextField(max_length=127, verbose_name="Название теста")
    description = models.TextField(max_length=255, verbose_name="Описание")
    count = models.PositiveIntegerField(verbose_name="Количество вопросов")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    questions = models.ManyToManyField(
        "TestsApp.Question", verbose_name="Вопросы", related_name="+", blank=True
    )
    max_result = models.IntegerField()
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse("inspect-test", kwargs={"test_slug": self.slug})

    def get_test_info(self):
        return {
            "title": self.title,
            "description": self.description,
            "time_create": self.time_create,
            "time_update": self.time_update,
            "questions_amount": self.count,
            "max_result": self.max_result,
            "slug": self.slug,
        }

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            "time_update",
            "title",
        )
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey("CoursesApp.Group", default=None, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.FloatField(default=0.0)
    is_passed = models.BooleanField(default=False, verbose_name="Пройден")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def get_result_info(self):
        return {
            "student": self.student.user.get_user_info(),
            "group_index": self.group.index,
            "max_result": self.test.max_result,
            "test_slug": self.test.slug,
            "result": self.result,
            "is_passed": self.is_passed,
            "result_slug": self.slug,
        }

    class Meta:
        verbose_name = "Результат студента"
        verbose_name_plural = "Результаты студентов"


class Question(models.Model):
    class QuestionType(models.TextChoices):
        single = "single"
        multiple = "multiple"

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, verbose_name="Вопрос")
    answers = models.ManyToManyField("TestsApp.Answer", related_name="+")
    max_points = models.PositiveIntegerField()
    qtype = models.CharField(
        max_length=8, choices=QuestionType.choices, default=QuestionType.single
    )

    def get_question_info(self):
        return {
            "question": self.question,
            "max_points": self.max_points,
            "qtype": self.qtype,
            "answers": list(answer.get_answer_info() for answer in self.answers.all()),
        }

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос для теста"
        verbose_name_plural = "Вопросы для тестов"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=255, verbose_name="Вариант ответа")
    is_correct = models.BooleanField(default=False)

    def get_answer_info(self):
        return {
            "answer": self.answer,
            "is_correct": self.is_correct,
        }

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ для теста"
        verbose_name_plural = "Ответы для тестов"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студентов"
