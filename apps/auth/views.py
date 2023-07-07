from django.shortcuts import redirect, render

from .forms import UserForm

def auth(request):
   error = ''
   if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('story')
      else: error = 'Некорректная форма'
   
   
   form = UserForm()
   data = {
      'form': form, 
      'error': error, 
   }
   
   return render(request, "auth/auth.html", data)
