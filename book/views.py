from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic

class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)




class BookCreateView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)

class BookUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = '/book/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)

class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)

def comment_view(request):
    comment = models.CommentBook.objects.all()
    return render(request, 'book_detail.html', {'book_comment': comment})
