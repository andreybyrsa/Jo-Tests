from django.shortcuts import redirect, render

def auth(request):
   
   return render(request, "auth/auth.html")
