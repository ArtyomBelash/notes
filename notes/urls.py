from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NotesListView.as_view(), name='index'),
    path('create', views.NoteCreateView.as_view(), name='create'),
    path('detail/<slug:slug>', views.NoteDetailView.as_view(), name='detail'),
    path('update/<slug:slug>', views.NoteUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>', views.NoteDeleteView.as_view(), name='delete'),
]
