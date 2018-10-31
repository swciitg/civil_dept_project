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

def StudentUpdateDetail(request, pk):
    student = get_object_or_404(models.Student, pk=pk)

    form = forms.UpdateStudDetail(instance=student)

    if request.method == 'POST':
        form = forms.UpdateStudDetail(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(student.get_absolute_url())

    return render(request, 'leave_portal/StudDetail.html', {'form':form, 'student':student})

def PendingRequest(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    forms = models.ApplyLeave.objects.filter(student=student)
    # forms=forms.cleaned_data()
    # forms = models.ApplyLeave.objects.get(student.id=pk)
    return render(request, 'leave_portal/pending_request.html', {'forms':forms})

from django.contrib.auth import authenticate ,login
from django.shortcuts import redirect

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = models.User.objects.get(username=username)
        print(user.username,user.password,password)
        if user.password is not password:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'leave_portal/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'leave_portal/login.html', {'error_message': 'Invalid login'})
    return render(request, 'leave_portal/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def signup(request):
    form = forms.SignUpUser()
    if request.method == "POST":
        form = forms.SignUpUser(request.POST)

        if form.is_valid():
            signup = form.save(commit=False)
            check = request.POST.get('person')

            if check is "student" :
                form.is_student=True

            elif check is "dppc" :
                form.is_dppc=True

            elif check is "office" :
                form.is_staff=True

            elif check is "hod" :
                form.is_hod=True
            form.save()
            return HttpResponse('done!!')
        else:
            return render(request, 'signup.html', {'error_message': 'Invalid login'})
    return render(request, 'signup.html' , {'form':form})
