from django.db import models
from apps.auth.models import Author


class Test(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.TextField(max_length=127, verbose_name="Название теста")
    description = models.TextField(max_length=255, verbose_name="Описание")
    count = models.IntegerField(verbose_name="Количество вопросов")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    date_expired = models.DateTimeField(
        auto_now=True, verbose_name="Дата истекания доступа к тесту"
    )
    questions = models.ManyToManyField("authorApp.Question", verbose_name="Вопросы", related_name='+')
    test_time = models.TimeField()
    max_result = models.IntegerField()
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("time_update", "title")
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    
    class QuestionType(models.TextChoices):
        single = "single"
        multiple = "mutiple"

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField(max_length=255, verbose_name="Вопрос")
    answers = models.ManyToManyField("authorApp.Answer", related_name='+')
    max_points = models.PositiveIntegerField()
    qtype = models.CharField(
        max_length=8, choices=QuestionType.choices, default=QuestionType.single
    )

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=255, verbose_name="Вариант ответа")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
