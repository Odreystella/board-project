from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from .mixins import LoggedOutOnlyView, LoggedInOnlyView

class LoginView(LoggedOutOnlyView, FormView):

    template_name = "users/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)  # get_success_url 호출함
    
    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("home")


def log_out(request):
    logout(request)
    return redirect(reverse("home"))


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("home")  

    def form_valid(self, form):
        form.save()                      # form.is_valid() 가 True라면 save
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)