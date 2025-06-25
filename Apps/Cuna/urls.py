from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import StudentListCreateAPIView
from . import views
from .views import student_dashboard




urlpatterns = [
    #vercel
    path('', views.home, name='home'),

    # Course URLs
    path('api/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<uuid:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    
    # Teacher URLs
    path('api/teachers/', views.TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    
    # Student URLs
    path('api/students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student-detail'),
    
    # Workload URLs
    path('api/workloads/', views.WorkloadListCreateView.as_view(), name='workload-list-create'),
    path('api/workloads/<int:pk>/', views.WorkloadDetailView.as_view(), name='workload-detail'),
    
    # Inscription URLs
    path('api/inscriptions/', views.InscriptionListCreateView.as_view(), name='inscription-list-create'),
    path('api/inscriptions/<int:pk>/', views.InscriptionDetailView.as_view(), name='inscription-detail'),
    
    path('api/announcements/', views.AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('api/announcements/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement-detail'),
    
    path('api/proxys/', views.ProxyListCreateView.as_view(), name='proxy-list-create'),
    path('api/proxys/<int:pk>/', views.ProxyDetailView.as_view(), name='proxy-detail'),

    path('api/yearcourses/', views.YearCourseListCreateView.as_view(), name='yearcourse-list-create'),
    path('api/yearcourses/<uuid:pk>/', views.YearCourseDetailView.as_view(), name='yearcourse-detail'),

    path('api/grades/', views.GradeListCreateView.as_view(), name='grade-list-create'),
    path('api/grades/<int:pk>/', views.GradeDetailView.as_view(), name='grade-detail'),
    path('api/students/<int:student_id>/grades/', views.StudentGradesView.as_view(), name='student-grades'),
    path('api/workloads/<int:workload_id>/grades/', views.WorkloadGradesView.as_view(), name='workload-grades'),

    # Authentication URLs
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/auth/profile/', views.ProfileView.as_view(), name='profile'),
    path('api/auth/status/', views.AuthStatusView.as_view(), name='auth-status'),
    
    # User management URLs
    path('api/users/', views.UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('api/profiles/', views.AllProfilesView.as_view(), name='all-profiles'),

    # Custom endpoints
    path('api/courses/statistics/', views.CourseStatisticsView.as_view(), name='course-statistics'),
    path('api/workloads/<int:workload_id>/students/', views.StudentsByWorkloadView.as_view(), name='workload-students'),
    path('students/<int:student_id>/dashboard/', student_dashboard, name='student-dashboard'),
]
# Permite formato de sufijo en URLs (ej: .json, .api)
urlpatterns = format_suffix_patterns(urlpatterns)
# Admin URL