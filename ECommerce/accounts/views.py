from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegiserUserForm

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request,('there was an error'))
            return redirect('login')
    else:
        return render(request, 'login.html')

def register_user(request):
    if request.method=='POST':
        form = RegiserUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('products')
        else:
            # print('invalid')
            context={'errors':form.errors, 'form':form}

    else:
        form = RegiserUserForm()
        context = {'form':form}

    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')