from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView


# Create your views here.

# template view
from books.models import Book, Author, Publisher


class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Books', 'Author', 'Publisher']
        return context


# list view
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# detail view
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher


