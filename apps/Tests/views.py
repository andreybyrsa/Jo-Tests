from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View
from django.contrib import messages

from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from core.utils.get_request_list import get_request_list

from .forms import TestCreateForm

from uuid import uuid4

from apps.auth.models import Author
from .models import Test, Question, Answer


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
    login_url = '/auth/'
    redirect_field_name = 'tests'

    def get(self, request):
        form = TestCreateForm
        header_def = self.get_user_header()
        context = dict(list({'form': form}.items())+list(header_def.items()))
        return render(request, 'Tests/CreateTestPage.html', context)

    def post(self, request):
        post = get_request_list(request.POST)
        author = Author.objects.get(user__id = request.user.id)
        try:
            test = Test.objects.create(
                author = author,
                title = request.POST['title'],
                description = request.POST['title'],
                count = post['count'],
                max_result = post['max_points'],
                slug = 'test' + str(uuid4()),
            )
            author.tests.add(test)

            for i in range(post['count']):
                    Q = Question.objects.create(
                        test = test,
                        question = post['questions'][i],
                        max_points = post['points'][i],
                        qtype = 'single' if len(post['rightAnwers'][i]) == 1 else 'multiple',
                    )
                    test.questions.add(Q)

                    for answer in post['answers'][i]:
                        A = Answer.objects.create(
                            question = Q,
                            answer = answer,
                            is_correct = True if answer in post['rightAnwers'][i] else False
                        )
                        Q.answers.add(A)
            return redirect('tests')
        except:
            messages.error(request, 'Ошибка создания теста')

def test_create(request):
    form = TestCreateForm
    print(request.POST)
    return render(request, "Tests/CreateTestPage.html", {"form": form})

def delete_test(request, test_slug):
    Test.objects.get(slug=test_slug).delete()
    return redirect("tests")
