from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Main view that renders the dashboard"""
    return render(request, 'Base/dashboard.html')
