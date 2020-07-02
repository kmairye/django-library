from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Author, Book, BookInstance

# Create your views here.


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10


class AuthorListView(ListView):
    model = Author
    template_name = 'article_list.html'
    paginate_by = 10


def index(request):
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_available_books = BookInstance.objects.filter(status='A').count()
    context = {
        'num_authors': num_authors,
        'num_books': num_books,
        'num_available_books': num_available_books
    }
    return render(request, 'library/index.html', context=context)
