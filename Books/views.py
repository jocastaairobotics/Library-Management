from django.shortcuts import render
from .models import Author, Category, Publication
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AuthorListView(ListView):
    model = Author
    template_name = "author/index.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = "author/create.html"
    success_url = "/books/authorlist"


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = "author/create.html"
    success_url = "/books/authorlist"


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author/delete.html"
    success_url = "/books/authorlist"

