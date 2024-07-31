from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('registration', views.CustomRegistrationView.as_view(), name='registration'),
    path('logout', views.CustomLogoutView.as_view(), name='logout')
]
