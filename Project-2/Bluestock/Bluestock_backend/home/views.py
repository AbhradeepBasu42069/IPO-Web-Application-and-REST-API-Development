# from django.shortcuts import render
# from .models import*
# #from django.urls import reverse

# # Create your views here.
# def home_view(request):
#     objt = IpoInfo.objects.get(id=1)
    
#     return render(request,'home/index.html',{
#         'obj':objt,
#     })

# def login_view(request):
    
    
#     return render(request,'home/login.html')

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def user_login(request):
    """
    Handle user login requests.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered login page or redirect to dashboard
    """
    if request.method == "POST":
        email_or_username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # First try to authenticate with username
            user = authenticate(request, username=email_or_username, password=password)
            
            # If that fails, try to find by email
            if user is None and '@' in email_or_username:
                try:
                    user_obj = User.objects.get(email=email_or_username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
                    
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home:dashboard'
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email/username or password")
        except Exception as e:
            messages.error(request, f"Login error: {str(e)}")
            
    return render(request, 'home/login.html', {
        'next': request.GET.get('next', '')
    })

# def user_register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
        
#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already taken")
#             else:
#                 User.objects.create_user(username=username, password=password)
#                 messages.success(request, "Registration successful! You can now log in.")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match")
#     return render(request, 'home/sigin.html')
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def user_register(request):
    """
    Handle user registration requests.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered registration page or JSON response with result
    """
    if request.method == 'GET':
        return render(request, 'home/sigin.html')
    
    try:
        data = request.POST
        
        # Validate required fields
        required_fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'confirm_password']
        if not all(field in data for field in required_fields):
            return JsonResponse({'error': 'Missing required fields'}, status=400)
            
        # Additional validation
        errors = []
        if len(data['password']) < 8:
            errors.append("Password must be at least 8 characters")
        if data['password'] != data['confirm_password']:
            errors.append("Passwords do not match")
        try:
            validate_email(data['email'])
            if User.objects.filter(email=data['email']).exists():
                errors.append("Email already registered")
        except ValidationError:
            errors.append("Invalid email address")
            
        # Validate phone number
        if 'phone' in data and (not data['phone'].isdigit() or len(data['phone']) != 10):
            errors.append("Phone number must be 10 digits")
            
        if errors:
            return JsonResponse({'errors': errors}, status=400)
            
        # Create user
        username = data['email'].split('@')[0]
        User.objects.create_user(
            username=username,
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        
        return JsonResponse({
            'message': 'Registration successful',
            'redirect': '/dashboard/'
        })
        
    except Exception as e:
        return JsonResponse({
            'error': 'Registration failed',
            'errors': [str(e)]
        }, status=400)

def user_logout(request):
    logout(request)
    return redirect('home:login')  # Redirect to the login page after logout

@login_required
def dashboard(request):
    return render(request, 'home/index.html')
