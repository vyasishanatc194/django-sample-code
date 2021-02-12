from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import UserLoginForm


class LoginView(View):
    template_name = 'authentication/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = UserLoginForm()
        return render(request, template_name=self.template_name, context={
            "form": form
        })

    def post(self, request):
        form = UserLoginForm(request.POST or None)
        nextRoute = request.GET.get('next', '/')
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect(nextRoute)
        return render(request, template_name=self.template_name, context={
            "form": form
        })


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')