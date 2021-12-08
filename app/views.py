from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.urls import reverse_lazy
from .models import Book , Auther


class BookListView(ListView):
    template_name = "book/book_list.html"
    model = Book


class BookDetailView(DetailView):
    template_name = "book/book_detail.html"
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    template_name = "book/book_create.html"
    model = Book
    fields = ['title','description', 'auther', 'rate']


class BookUpdateView(UpdateView):
    template_name = "book/book_update.html"
    model = Book
    fields = ['title','description', 'auther', 'rate']


class BookDeleteView(DeleteView):
    template_name = "book/book_delete.html"
    model = Book
    success_url = reverse_lazy("book_list")

#=================================================
class AutherListView(ListView):
    template_name = "auther/auther_list.html"
    model = Auther


class AutherDetailView(DetailView):
    template_name = "auther/auther_detail.html"
    model = Auther
    context_object_name = 'auther'


class AutherCreateView(CreateView):
    template_name = "auther/auther_create.html"
    model = Auther
    fields = ['name', 'phone_number','location']


class AutherUpdateView(UpdateView):
    template_name = "auther/auther_update.html"
    model = Auther
    fields = ['name', 'phone_number','location']


class AutherDeleteView(DeleteView):
    template_name = "auther/auther_delete.html"
    model = Auther
    success_url = reverse_lazy("auther_list")
