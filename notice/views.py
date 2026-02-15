from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import Notice
from django.contrib.auth.models import User

# Check if user is admin
def is_admin(user):
    return user.is_staff

# 🌐 Public Home
def home(request):
    notices = Notice.objects.all().order_by('-date_posted')[:3]
    return render(request, "home.html", {"notices": notices})

def about(request):
    return render(request, "about.html")

def departments(request):
    return render(request, "departments.html")

def academic_event(request):
    return render(request, "academic_event.html")

def contact(request):
    return render(request, "contact.html")


# 🔐 Admin Login
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "admin_login.html", {"error": "Invalid admin credentials"})
    return render(request, "admin_login.html")

# 🔐 Student Login
def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect("student_dashboard")
        else:
            return render(request, "student_login.html", {"error": "Invalid student credentials"})
    return render(request, "student_login.html")

# 🚪 Logout
@login_required(login_url='student_login')
def logout_view(request):
    logout(request)
    return redirect("home")

# 🎓 Admin Dashboard
@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def admin_dashboard(request):
    notices = Notice.objects.all().order_by('-date_posted')
    return render(request, "admin_dashboard.html", {"notices": notices})

# ➕ Add Notice
@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def add_notice(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        Notice.objects.create(title=title, description=description, file=file, created_by=request.user)
        return redirect("admin_dashboard")
    return render(request, "add_notice.html")

# ❌ Delete Notice
@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.delete()
    return redirect("admin_dashboard")

# 🎓 Student Dashboard
@login_required(login_url='student_login')
def student_dashboard(request):
    notices = Notice.objects.all().order_by('-date_posted')
    return render(request, "student_dashboard.html", {"notices": notices})