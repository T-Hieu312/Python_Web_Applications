from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Đăng ký người dùng mới"""
    if request.method != 'POST':
        # Hiển thị form đăng ký trống
        form = UserCreationForm()
    else:
        # Xử lý form đã điền
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Đăng nhập và chuyển hướng về trang chủ
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Hiển thị form trống hoặc không hợp lệ
    context = {'form': form}
    return render(request, 'registration/register.html', context)