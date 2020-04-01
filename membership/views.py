from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .forms import ModifiedUserCreationForm
from .models import Loan, BookInstance

# VIEWS
# Latest at the top, oldest at the bottom


def loan_book(request):
    if request.method == "POST":
        match_book_id = request.POST["bookID"]
        book_instance = get_object_or_404(BookInstance, pk=match_book_id)
        book_instance.status = 'N'
        book_instance.save()

        user_instance = request.user

        newLoan = Loan()
        newLoan.user = user_instance
        newLoan.book = book_instance
        newLoan.save()
    return HttpResponseRedirect(reverse('profile'))


@login_required()
def profile(request):
    user = request.user
    staff_bool = user.profile.staff
    user_loans = Loan.objects.filter(user=user)
    all_book_instances = BookInstance.objects.all()
    context = {
        'user': user,
        'staff_bool': staff_bool,
        'user_loan_objects': user_loans,
        'all_book_instances': all_book_instances,
    }
    return render(request, 'membership/profile.html', context=context)


def logout_view(request):
    logout(request)
    return render(request, ('membership/logged_out.html'))


def login_view(request):

    context = {}

    # Double check that user is not already logged in, return if they are
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    # Check request method
    if request.method == 'POST':
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            # Pass error message
            context = {
                'error': 'One or more fields are incorrect.'
            }

    return render(request, 'membership/login.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = ModifiedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = ModifiedUserCreationForm()
    return render(request, 'membership/signup.html', {'form': form})


def index(request):
    num_members = User.objects.count()
    context = {
        'num_members': num_members,
    }
    return render(request, 'membership/index.html', context=context)
