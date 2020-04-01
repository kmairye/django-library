from django.contrib import admin
from .models import Profile, Loan, BookInstance

# Register your models here.

admin.site.register(Profile)

# admin.site.register(Loan)
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    """ Customize the way loans are displayed in admin page """
    list_display = ('book', 'user', 'is_overdue')
    fields = ['book', 'user', 'date_of_loan', 'date_of_return']
