# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UpdateProfileForm

class UserProfileView(LoginRequiredMixin, View):
    login_url = '/auth/'
    redirect_field_name = 'next'

    def get(self, request):
        user = request.user
        form = UpdateProfileForm(instance=user)
        context = {'user': user, 'form': form}
        return render(request, 'Profile/ProfilePage.html', context)

    def post(self, request):
        user = request.user
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')

        context = {'user': user, 'form': form}
        return render(request, 'Profile/ProfilePage.html', context)

