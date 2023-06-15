from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news})

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # автоматическая аутентификация пользователя после успешной регистрации
            login(request, user)
            return redirect('main:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
        # сохраняем данные в полях формы, если вход не был выполнен
        else:
            form.fields['username'].widget.attrs['value'] = request.POST.get('username')
            form.fields['password'].widget.attrs['value'] = request.POST.get('password')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})
        
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'main/edit.html', {'form': form})