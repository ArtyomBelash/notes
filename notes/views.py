from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import NoteCreateAndUpdateForm
from .models import Note
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesListView(generic.ListView):
    context_object_name = 'notes'
    template_name = 'notes/index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            owner = self.request.user
            return Note.objects.filter(owner=owner)


class NoteDetailView(generic.DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/detail_note.html'
    slug_field = 'slug'


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    model = Note
    slug_field = 'slug'
    template_name = 'notes/update_note.html'
    form_class = NoteCreateAndUpdateForm

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Note, slug=slug)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('notes:detail', kwargs={'slug': slug})


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    model = Note
    form_class = NoteCreateAndUpdateForm
    success_url = reverse_lazy('notes:index')
    template_name = 'notes/create_note.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = 'login'
    model = Note
    success_url = reverse_lazy('notes:index')
    template_name = 'notes/confirm_delete_note.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Note, slug=self.kwargs['slug'])
        return obj
