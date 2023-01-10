from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms


class ParserView(ListView):
    model = models.BookParser
    template_name = "book_list.html"

    def get_queryset(self):
        return models.BookParser.objects.all()


class ParserFormView(FormView):
    template_name = "parser_book.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("<h2>Данные взяты.............</h2>")
        else:
            return super(ParserFormView).post(request, *args, *kwargs)
