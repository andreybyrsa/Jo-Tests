from django.shortcuts import redirect, render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from apps.auth.models import Author
from .models import Test


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


def test_create(request):
    return render(request, "Tests/InfoSideBarTest.html")

def delete_test(request, test_slug):
    Test.objects.get(slug=test_slug).delete()
    return redirect('tests')
