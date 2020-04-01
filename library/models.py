from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Book(models.Model):
    TYPE_CHOICES = (
        ('BO', 'Book'),
        ('MA', 'Magazine')
    )
    type = models.CharField(max_length=2, default='BO', blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    first_published = models.CharField(
        max_length=4, help_text="Enter year in format YYYY. Must be four digits", blank=True, null=True)

    summary = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", blank=True, null=True)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    STATUS_CHOICES = (
        ('A', 'Available'),
        ('N', 'Not available')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=255)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.book.title
