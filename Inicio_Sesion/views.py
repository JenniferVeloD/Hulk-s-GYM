from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirige al admin de Django
            return redirect(reverse('admin:index'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
