from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Memomodel

# Create your views here.
class Memolist(ListView):
    template_name='list.html'
    model=Memomodel

class Memocreate(CreateView):
    template_name='create.html'
    model=Memomodel
    fields=['タイトル','本文']
    success_url=reverse_lazy('list')

class Memodetail(DetailView):
    template_name='detail.html'
    model=Memomodel

class Memodelete(DeleteView):
    template_name='delete.html'
    model=Memomodel
    success_url=reverse_lazy('list')

class Memoupdate(UpdateView):
    template_name='update.html'
    model=Memomodel
    fields=['タイトル','本文']
    success_url=reverse_lazy('list')