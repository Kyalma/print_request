from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from pullapp.forms import UserSignupForm


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'pullapp/signup.html', {'form': form})
