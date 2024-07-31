from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Profile
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = "profiles/login.html"
    redirect_authenticated_user = True
    extra_context = None


class CustomRegistrationView(generic.CreateView):
    model = Profile
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('notes:index')
    template_name = 'profiles/registration.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)


class CustomLogoutView(generic.View):

    def get(self, request):
        if self.request.user.is_authenticated:
            logout(request)
            return redirect('notes:index')
