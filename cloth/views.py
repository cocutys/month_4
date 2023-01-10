from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms

class ClothListView(ListView):
    queryset = models.Cloth.objects.filter().order_by('-id')
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.Cloth.objects.filter().order_by('-id')

class ClothListViewRetro(ListView):
    queryset = models.Cloth.objects.filter(tags__name='retro').order_by('-id')
    template_name = "retro_clothes_list.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='retro').order_by('-id')

class ClothListViewUnisex(ListView):
    queryset = models.Cloth.objects.filter(tags__name='unisex').order_by('-id')
    template_name = "unisex_clothes_list.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='unisex').order_by('-id')

class ClothListViewFemale(ListView):
    queryset = models.Cloth.objects.filter(tags__name='Female').order_by('-id')
    template_name = "female_clothes_list.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Female').order_by('-id')

class ClothListViewMale(ListView):
    queryset = models.Cloth.objects.filter(tags__name='Male').order_by('-id')
    template_name = "male_clothes_list.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Male').order_by('-id')



class OrderCreateView(CreateView):
    template_name = "create_order.html"
    form_class = forms.OrderForm
    success_url = "/cloth/"
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
