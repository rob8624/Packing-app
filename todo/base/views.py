from django.shortcuts import render
from .models import Box, Item
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


class ItemList(ListView):
    model = Item
    context_object_name = 'items'


class BoxList(ListView):
    model = Box
    context_object_name = 'boxes'


class BoxDetail(DetailView):
    model = Box
    context_object_name = 'box'
    template_name = 'base/boxdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_items'] = Box.get_items(self.object)
        return context


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'boxed']
    success_url = reverse_lazy('items')


class BoxCreateView(CreateView):
    model = Box
    fields = ['number']
    success_url = reverse_lazy('boxes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_count'] = Box.boxes.count()
        return context