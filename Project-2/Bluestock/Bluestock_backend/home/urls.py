# from django.urls import path
# from . import views


# urlpatterns = [
#     path('',views.home_view,name="home"),
#     path('login/',views.login_view,name="login"),
    
# ]

from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    
]