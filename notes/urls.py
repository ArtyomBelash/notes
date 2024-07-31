from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.CreateNote.as_view(), name='create'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('update/<slug:slug>', views.NoteUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>', views.DeleteNote.as_view(), name='delete'),
]
