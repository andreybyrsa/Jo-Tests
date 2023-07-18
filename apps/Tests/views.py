from typing import Any, Dict
from django.db.models import F
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, DetailView
from django.contrib import messages

from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from core.utils.get_request_list import get_request_list
from core.utils.get_unique_slug import get_unique_slug
from core.utils.get_student_choices import get_student_choices

from .forms import TestCreateForm

from uuid import uuid4

from apps.auth.models import Author, Student
from apps.Courses.models import CourseTest, Course
from .models import Test, Question, Answer, StudentResult, Choice


class ViewTests(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    """Список тестов - Author, Teacher"""

    model = Test
    login_url = "/auth"
    template_name = "Tests/TestsPage.html"
    context_object_name = "tests"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        json_tests = list(test.get_test_info() for test in context["tests"])
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar("test")

        return dict(
            list(context.items())
            + list(header_def.items())
            + list(sidebar_def.items())
            + list({"json_tests": json_tests}.items())
        )

    def get_queryset(self):
        current_user = self.request.user

        if current_user.role == "teacher":
            return Test.objects.all()

        author = Author.objects.get(user=current_user)
        return author.tests.all()


class CreateTest(LoginRequiredMixin, HeaderMixin, View):
    """Создание теста - Author"""

    login_url = "/auth/"
    redirect_field_name = "tests"

    def get(self, request):
        current_user = request.user
        if current_user.role != "author":
            messages.error(request, "Доступ запрещен")
            return redirect("profile")
        form = TestCreateForm
        header_def = self.get_user_header()
        context = dict(list({"form": form}.items()) + list(header_def.items()))

        return render(request, "Tests/CreateTestPage.html", context)

    def post(self, request):
        current_user = request.user
        post = get_request_list(request.POST)
        author = Author.objects.get(user__id=current_user.id)

        try:
            test = Test.objects.create(
                author=author,
                title=request.POST["title"],
                description=request.POST["description"],
                count=post["count"],
                max_result=post["max_points"],
                slug=get_unique_slug(Test, request.POST["title"]),
            )
            author.tests.add(test)

            for i in range(post["count"]):
                question = Question.objects.create(
                    test=test,
                    question=post["questions"][i],
                    max_points=post["points"][i],
                    qtype="single" if len(post["rightAnwers"][i]) == 1 else "multiple",
                )
                test.questions.add(question)

                for post_answer in post["answers"][i]:
                    answer = Answer.objects.create(
                        question=question,
                        answer=post_answer,
                        is_correct=True
                        if post_answer in post["rightAnwers"][i]
                        else False,
                    )
                    question.answers.add(answer)

            messages.success(request, "Успешное создание теста!")
            return redirect("tests")
        except:
            messages.error(request, "Ошибка создания теста")
            return redirect("tests")


class EditTest(LoginRequiredMixin, HeaderMixin, View):
    """Редактирование теста - Author"""

    login_url = "/auth/"
    redirect_field_name = "tests"

    def get(self, request, test_slug):
        current_user = request.user
        if current_user.role != "author":
            messages.error(request, "Доступ запрещен")
            return redirect("profile")
        test = Test.objects.get(slug=test_slug)
        form = TestCreateForm(instance=test)
        questions = Question.objects.filter(test__id=test.id)
        questions_info = list(question.get_question_info() for question in questions)
        header_def = self.get_user_header()
        context = dict(
            list({"form": form}.items())
            + list(header_def.items())
            + list(
                {"test": test.get_test_info(), "questions_info": questions_info}.items()
            )
        )

        return render(request, "Tests/CreateTestPage.html", context)

    def post(self, request, test_slug):
        test = Test.objects.get(slug=test_slug)
        post = get_request_list(request.POST)
        try:
            test.title = request.POST["title"]
            test.description = request.POST["description"]
            test.max_result = post["max_points"]
            test.count = post["count"]

            Question.objects.filter(test__id=test.id).delete()

            for i in range(post["count"]):
                question = Question.objects.create(
                    test=test,
                    question=post["questions"][i],
                    max_points=post["points"][i],
                    qtype="single" if len(post["rightAnwers"][i]) == 1 else "multiple",
                )
                test.questions.add(question)

                for post_answer in post["answers"][i]:
                    answer = Answer.objects.create(
                        question=question,
                        answer=post_answer,
                        is_correct=True
                        if post_answer in post["rightAnwers"][i]
                        else False,
                    )
                    question.answers.add(answer)

            test.save()
            messages.success(request, "Успешное обновление теста")
            return redirect("tests")

        except:
            messages.error(request, "Ошибка редактирования теста")
            return redirect("tests")


class InspectTest(LoginRequiredMixin, HeaderMixin, DetailView):
    model = Test
    template_name = "Tests/InspectTestPage.html"
    login_url = "/auth/"
    redirect_field_name = "tests"
    slug_url_kwarg = "test_slug"
    context_object_name = "test"

    def get_context_data(self, *, object_list=None, **kwargs):
        current_user = self.request.user

        if current_user.role != "teacher":
            messages.error(self.request, "Доступ запрещен")
            return redirect("profile")

        header_def = self.get_user_header()
        context = super().get_context_data(**kwargs)
        json_question_info = list(
            question.get_question_info() for question in context["test"].questions.all()
        )

        return dict(
            list(context.items())
            + list(header_def.items())
            + list({"json_question_info": json_question_info}.items())
        )


class IspectResult(LoginRequiredMixin, HeaderMixin, DetailView):
    model = StudentResult
    template_name = "Tests/TestResultPage.html"
    login_url = "/auth/"
    slug_url_kwarg = "result_slug"
    context_object_name = "result"

    def get_context_data(self, *, object_list=None, **kwargs):
        current_user = self.request.user

        if current_user.role not in ("teacher", "student"):
            messages(self.request, "Доступ запрещен")
            return redirect("")

        header_def = self.get_user_header()
        context = super().get_context_data(**kwargs)
        test = Test.objects.get(slug=context["result"].test.slug)
        json_questions_info = list(
            question.get_question_info() for question in test.questions.all()
        )
        json_choices = {}

        for json_question_info in json_questions_info:
            json_choices[f'{json_question_info["id"]}'] = []
            choices = context["result"].choises.filter(
                question__id=json_question_info["id"]
            )
            result = 0
            right_answers = 0

            for answer in json_question_info["answers"]:
                if answer["is_correct"]:
                    right_answers += 1

            wrong_answers = len(json_question_info["answers"]) - right_answers
            for choice in choices:
                if choice.is_selected:
                    if choice.answer.is_correct:
                        result += json_question_info["max_points"] / right_answers
                    else:
                        result -= json_question_info["max_points"] / wrong_answers
                json_choices[f'{json_question_info["id"]}'].append(
                    choice.get_choice_info()
                )

            json_choices[f'{json_question_info["id"]}'].append(
                result if result > 0 else 0
            )

        return dict(
            list(context.items())
            + list(header_def.items())
            + list(
                {
                    "test": test,
                    "json_question_info": json_questions_info,
                    "json_choices": json_choices,
                }.items()
            )
        )


class PassTest(HeaderMixin, LoginRequiredMixin, View):
    """Прохождение теста - Student"""

    login_url = "/auth/"
    redirect_field_name = "tests"

    def get(self, request, test_slug):
        current_user = request.user

        if current_user.role != "student":
            messages.error(request, "Тест могут проходить только студенты")
            return redirect("profile")

        course_slug = self.request.META.get("HTTP_REFERER").split("/")[-1]
        test = Test.objects.get(slug=test_slug)
        course_test = CourseTest.objects.get(test=test, course__slug=course_slug)

        if StudentResult.objects.filter(
            test=test, student__user=current_user, course__slug=course_slug
        ).exists():
            messages.error(request, "Тест уже пройден")
            return redirect("profile")

        questions = test.questions.all()
        json_questions_info = list(
            question.get_question_info() for question in questions
        )
        header_def = self.get_user_header()
        context = dict(
            list(header_def.items())
            + list(
                {
                    "course_slug": course_slug,
                    "json_questions_info": json_questions_info,
                    "json_test": course_test.get_test_in_course_info(),
                }.items()
            )
        )

        return render(request, "Tests/PassTestPage.html", context)

    def post(self, request, test_slug):
        current_user = request.user
        student = Student.objects.get(user__id=current_user.id)
        course_slug = request.POST["course-slug"]
        course = Course.objects.get(slug=course_slug)
        test = Test.objects.get(slug=test_slug)

        try:
            test_result = StudentResult.objects.create(
                student=student,
                course=course,
                test=test,
                is_passed=True,
                slug="result-" + get_unique_slug(StudentResult, test_slug),
            )

            post_questions = get_student_choices(request.POST)
            result = 0

            for post_question in post_questions:
                question = Question.objects.get(id=int(post_question["question"]))
                answers = question.answers.all()
                right_answers = question.answers.filter(is_correct=True).count()
                wrong_answers = question.answers.filter(is_correct=False).count()
                question_result = 0

                for answer in answers:
                    choice = Choice.objects.create(
                        question=question,
                        student=student,
                        student_result=test_result,
                        answer=answer,
                        is_selected=True
                        if answer.answer in post_question["choosen"]
                        else False,
                    )
                    test_result.choises.add(choice)

                    if choice.is_selected:
                        if choice.answer.is_correct:
                            question_result += question.max_points / right_answers
                        else:
                            question_result -= question.max_points / wrong_answers
                result += question_result if question_result > 0 else 0

            test_result.result = result
            test_result.save()
            Course.objects.filter(slug=course.slug).update(
                progress=(F("progress") + result)
            )
            student.result_tests.add(test_result)

            messages.success(request, f'Вы успешно прошли тест "{test.title}"')
            return redirect("inspect-course", course_slug=course_slug)

        except:
            messages.error(request, f'Ошибка прохождения теста "{test.title}"')
            return redirect("inspect-course", course_slug=course_slug)


def delete_test(request, test_slug):
    """Удаление теста - Author"""

    Test.objects.get(slug=test_slug).delete()
    return redirect("tests")
