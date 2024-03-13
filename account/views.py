from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'sign-in.html', {'error': 'Email or Password is incorrect'})
    return render(request, 'sign-in.html')

def signup(request):
    if request.method=='POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'sign-up.html')


def logout_view(request):
    logout(request)
    return redirect('login')