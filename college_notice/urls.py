from django.contrib import admin
from django.urls import path
from notice import views

urlpatterns = [
    # 🔧 Django Admin Panel
    path('admin/', admin.site.urls),

    # 🌐 Public Home
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('academic-event/', views.academic_event, name='academic_event'),
    path('contact/', views.contact, name='contact'),

    # 🔐 Admin Login & Dashboard
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('delete-notice/<int:notice_id>/', views.delete_notice, name='delete_notice'),

    # 🔐 Student Login & Dashboard
    path('student-login/', views.student_login, name='student_login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    # 🚪 Logout
    path('logout/', views.logout_view, name='logout'),
]