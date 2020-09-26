
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Student
from .models import WeeklyEntry

from .forms import StudentForm
from .forms import WeeklyEntryForm



# Create your views here.

def add_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        print(student_form)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.save()
            return redirect('student-list')
    else:
        student_form = StudentForm()
    return render(request, 'covid_tracker/add_student.html', {'student_form': student_form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            post = student_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('student-list')
    else:
        student_form = StudentForm(instance=student)
    return render(request, 'covid_tracker/add_student.html', {'student_form': student_form})

def weekly_entry_edit(request, pk):
    entry = get_object_or_404(WeeklyEntry, pk=pk)
    if request.method == "POST":
        weekly_entry_form = WeeklyEntryForm(request.POST, instance=entry)
        if weekly_entry_form.is_valid():
            post = weekly_entry_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('student-list')
    else:
        weekly_entry_form = WeeklyEntryForm(instance=entry)
    return render(request, 'covid_tracker/add_weekly_entry.html', {'weekly_entry_form': weekly_entry_form})




#FIGURING OUT logbook entries

def add_weekly_entry(request, pk):
    if request.method == "POST":
        weekly_entry_form = WeeklyEntryForm(request.POST)
        print(weekly_entry_form)
        if weekly_entry_form.is_valid():
            weekly_entry = weekly_entry_form.save(commit=False)
            weekly_entry.save()
            return redirect('student-list')
    else:
        weekly_entry_form = WeeklyEntryForm
    return render(request, 'covid_tracker/add_weekly_entry.html', {'weekly_entry_form': weekly_entry_form})






class StudentListView(ListView):
    model = Student

    def student_display(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class StudentDetailView(DetailView):
    model = Student 
    
    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['pk'])
        #pilot_logs = get_object_or_404(LogbookEntry, pk=kwargs['pk'])
        lbe = WeeklyEntry.objects.filter(student_id=kwargs['pk'])
        context = {'student': student, 'student_logs': lbe}
        return render(request, 'covid_tracker/student_detail.html', context)
     
class LogbookListView(ListView):
    model = LogbookEntry

    def logbook_entry_display(self, request, *args, **kwargs):
        logbook_entry = get_object_or_404(LogbookEntry, pk=kwargs['pk'])
        context = {'weekly_entry': weekly_entry} 
        return render(request, 'covid_tracker/weekly_entry_list.html', context)

