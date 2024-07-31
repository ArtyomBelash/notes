from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = "profiles/login.html"
    redirect_authenticated_user = True
    extra_context = None
