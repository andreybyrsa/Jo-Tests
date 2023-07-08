from django.shortcuts import render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from .models import Test, Author

# СписокТестов(author, teacher)


class ViewTests(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    model = Test
    login_url = "/auth/"
    template_name = "author/tests.html"
    context_object_name = "tests"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar("test")
        return dict(
            list(context.items()) + list(header_def.items()) + list(sidebar_def.items())
        )

    def get_querryset(self):
        current_user = self.request.user
        if current_user.role == "teacher":
            return Test.objects.all()
        author = Author.objects.get(user=current_user)
        return author.tests.all()


def test_create(request):
    return render(request, "author/InfoSideBarTest.html")
