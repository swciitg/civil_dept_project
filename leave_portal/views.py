from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
# Create your views here.

def index(request):
    return HttpResponse("HelloWorld!!")

class StudentListView(generic.ListView):
    model = models.Student

class StudentDetailView(generic.DetailView):
    model = models.Student


def ApplyLeave(request,pk):
    student = get_object_or_404(models.Student, pk=pk)
    form = forms.LeaveForm()

    if request.method == 'POST':
        form = forms.LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.student = student
            leave.save()
            return HttpResponseRedirect(student.get_absolute_url())
    return render(request, 'leave_portal/leaveform.html', {'student':student, 'form':form})

def ApplyLeaveEdit(request, pk, leave_id):
    student = get_object_or_404(models.Student, pk=pk)
    leave = get_object_or_404(models.ApplyLeave, pk=leave_id, student=student)

    form = forms.LeaveForm(instance=leave)

    if request.method == 'POST':
        form = forms.LeaveForm(instance=leave, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(student.get_absolute_url())

    return render(request, 'leave_portal/leaveform.html', {'form':form, 'student':student})
