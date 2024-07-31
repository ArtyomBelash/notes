from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls', namespace='notes')),
    path('profile/', include('profiles.urls', namespace='profile')),

]
