from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Note
from django.views import generic


def index(request):
    owner = request.user
    notes = Note.objects.filter(owner=owner)
    return render(request, 'notes/index.html', {'notes': notes})


def detail(request, slug):
    note = Note.objects.get(slug=slug)
    return render(request, 'notes/detail.html', {'note': note})


class NoteUpdateView(generic.UpdateView):
    model = Note
    slug_field = 'slug'
    # fields = ('name', 'description')
    template_name = 'notes/update.html'
    form_class = NoteForm

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Note, slug=slug)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('detail', kwargs={'slug': slug})


class CreateNote(generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('index')
    template_name = 'notes/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class DeleteNote(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('index')
    template_name = 'notes/delete.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Note, slug=self.kwargs['slug'])
        return obj
