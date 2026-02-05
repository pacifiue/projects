from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.home, name='login'),  # login page
    path('register/', views.register, name='register'),  # user registration
    path('dashboard/', views.dashboard, name='dashboard'),  # dashboard
    path('logout/', views.logout, name='logout'),  # logout

    # Student
    path('student/register/', views.student_register, name='student_register'),
    path('students/', views.student_list, name='student_list'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path("student/report/<int:id>/", views.student_report, name="student_report"),


    # Teacher
    path('teacher/register/', views.teacher_register, name='teacher_register'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:id>/', views.delete_teacher, name='delete_teacher'), 

    # Marks
    path('marks/', views.mark_entry, name='mark_entry'),

    # Success page (after student registration)
    path('success/', lambda request: render(request, "success.html"), name='success'),
]
