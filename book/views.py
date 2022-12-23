from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book_object': book})

def book_view_detail(request, id):
    book_detail = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'object_detail': book_detail})

def add_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>Книга успешно добавлена</h1>')
    else:
        form = forms.BookForm()

    return render(request, 'create_book.html', {'form': form})