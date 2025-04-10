from django.contrib import admin

# Register your models here.

# from .models import User, IpoInfo

# # Register your models here
# admin.site.register(User)
# admin.site.register(IpoInfo)
from django.contrib.auth.models import User  # Built-in User model
from .models import IpoInfo

from django.contrib import admin
from .models import User, IpoInfo

admin.site.register(User)
admin.site.register(IpoInfo)