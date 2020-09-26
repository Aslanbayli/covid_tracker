from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
from .views import StudentListView
from .views import StudentDetailView

from .views import WeeklyEntryListView



urlpatterns = [
    path('add_student', views.add_student, name='add_student'),
    path('student/<int:pk>/add_weekly_entry', views.add_weekly_entry, name='add_weekly_entry'),

    path('student_display', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),

    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('weekly_entry_edit/<int:pk>', views.weekly_entry_edit, name='weekly-entry-edit'),



    


    


    
]