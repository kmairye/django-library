from django.urls import path
from . import views
from membership import views as membershipview
# URL PATTERNS

urlpatterns = [
    path('', views.index, name="index"),
    path('authors/', views.AuthorListView.as_view(), name="author-list"),
    path('books/', views.BookListView.as_view(), name="book-list"),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name="author-detail"),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book-detail"),
]
