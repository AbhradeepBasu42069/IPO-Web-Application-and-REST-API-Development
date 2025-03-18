from multiprocessing import AuthenticationError
from urllib import request
from django.shortcuts import redirect, render

import login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = AuthenticationError(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login/login.html')
