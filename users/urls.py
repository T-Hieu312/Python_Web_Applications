from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Bao gồm các URL xác thực mặc định
    path('', include('django.contrib.auth.urls')),
    # Trang đăng ký
    path('register/', views.register, name='register'),
]