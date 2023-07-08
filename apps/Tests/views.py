from django.shortcuts import render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from apps.auth.models import Author
from .models import Test

# СписокТестов(author, teacher)


class ViewTests(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    model = Test
    login_url = "/auth"
    template_name = "Tests/TestsPage.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar("test")

        tests = self.get_queryset()
        json_tests = list(test.get_test_info() for test in tests)

        return {
            "json_tests": json_tests,
            "header": list(header_def["header"]),
            "test_side_bar": list(sidebar_def["info"]),
        }

    def get_queryset(self):
        current_user = self.request.user
        if current_user.role == "teacher":
            return Test.objects.all()

        author = Author.objects.get(user=current_user)
        return author.tests.all()


def test_create(request):
    return render(request, "Tests/InfoSideBarTest.html")
