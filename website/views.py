from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()

    # Check if trying to log in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in, try again.")

    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.warning(request, "You must be logged in to view that page.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully.")
    else:
        messages.warning(request, "You must be logged in to do that.")
    return redirect('home')


def add_record(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to do that.")
        return redirect('home')

    form = AddRecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Record added successfully.")
        return redirect('home')
        
    return render(request, 'add_record.html', {'form': form})


def update_record(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to do that.")
        return redirect('home')

    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Record updated successfully.")
        return redirect('home')

    return render(request, 'update_record.html', {'form': form})
