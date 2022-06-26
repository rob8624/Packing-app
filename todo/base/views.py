from django.shortcuts import render
from .models import Box, Item
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.views.decorators.http import require_http_methods
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import PackForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect



class ItemList(ListView):
    model = Item
    context_object_name = 'items'


class BoxList(ListView):
    model = Box
    context_object_name = 'boxes'

    def get_context_data(self, **kwargs):
        context = super(BoxList, self).get_context_data(**kwargs)
        context['form'] = BoxCreateView
        return context


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
    fields = ['number', 'additional']
    success_url = reverse_lazy('boxes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_count'] = Box.boxes.count()
        return context



def add_item(request):
    name = request.POST.get('itemname')
    Item.objects.create(name=name)
    items = Item.objects.all()



    return render(request, 'base/partials/list_items.html', {'items': items})


@require_http_methods(['DELETE'])
def delete_item(request, pk):
    Item.objects.filter(pk=pk).delete()
    items = Item.objects.all()
    return render(request, 'base/partials/list_items.html', {'items': items})



def search_items(request):
    search_text = request.POST.get('search')

    results = Item.objects.filter(name__icontains=search_text)
    context = {'results' : results }
    return render(request, 'base/partials/search-results.html', context)


def pack_item(request, pk):
    #get item from front end (pack button)
   item = Item.objects.get(pk=pk)


   if request.method == 'POST':
       form = PackForm(request.POST)
   if form.is_valid():
       item.boxed = form.cleaned_data['pack']
       item.save()
       #box =  form.cleaned_data['pack']
       #box_num = item.boxed = box

       #print (f"{item} packind into {box_num}")

       return redirect ('items')
   else:
       form = PackForm()

   context = {
       'form': form,

    }

   return render(request, 'base/pack_form.html', context)
















