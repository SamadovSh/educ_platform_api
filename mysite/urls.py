"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from courses.api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', api_views.CourseListView.as_view(), name='api_post_list'),
    path('dashboard/<pk>', api_views.CourseDetailView.as_view(), name='api_post_detail'),
    path('dashboard/teachers/', api_views.TeacherListView.as_view(), name='api_teacher'),
    path('dashboard/teachers/<pk>', api_views.TeacherDetailView.as_view(), name='api_detail_teacher'),
    path('dashboard/students/', api_views.StudentListView.as_view(), name='api_students'),
    path('dashboard/students/<pk>', api_views.StudentDetailView.as_view(), name='api_students_courses'),
]
