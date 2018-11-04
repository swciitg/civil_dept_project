from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
from users.models import CustomUser

# Create your views here.


from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    if request.user.person=='student':
        student = models.Student.objects.filter(user=request.user)
        if not student :
            form = forms.UpdateStudDetail()
            if request.method=='POST' :
                form = forms.UpdateStudDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                else:
                    print(form)
                    print("dsaasdsa")
                    #we are getting an error
                return redirect('leave_portal:dashboard')
            else :
                return render(request,'leave_portal/StudDetail.html', {'form':form , 'student':request.user.username} )
        else:
            student = models.Student.objects.get(user=request.user)
            return render(request,'leave_portal/dashboard.html',{'user':request.user , 'student':student})

    elif request.user.person=='dppc':
        dppc = models.Dppc.objects.filter(user=request.user)
        if not dppc :
            form = forms.UpdateDppcDetail()
            if request.method=='POST' :
                form = forms.UpdateDppcDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('leave_portal:dashboard')
            else :
                return render(request,'leave_portal/dppc_update_detail.html', {'form':form , 'dppc':request.user.username} )
        else:
            authorized = models.Dppc.objects.get(user=request.user)
            return render(request,'leave_portal/authorized_dashboard.html',{'user':request.user , 'authorized':authorized})

    elif request.user.person=='hod':
        hod = models.Hod.objects.filter(user=request.user)
        if not hod :
            form = forms.UpdateHodDetail()
            if request.method=='POST' :
                form = forms.UpdateHodDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('leave_portal:dashboard')
            else :
                return render(request,'leave_portal/dppc_update_detail.html', {'form':form , 'dppc':request.user.username} )
        else:
            authorized = models.Hod.objects.get(user=request.user)
            return render(request,'leave_portal/authorized_dashboard.html',{'user':request.user , 'authorized':authorized})

    elif request.user.person=='staff':
        staff = models.Staff.objects.filter(user=request.user)
        if not staff :
            form = forms.UpdateStaffDetail()
            if request.method=='POST' :
                form = forms.UpdateStaffDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('leave_portal:dashboard')
            else :
                return render(request,'leave_portal/dppc_update_detail.html', {'form':form , 'dppc':request.user.username} )
        else:
            authorized = models.Staff.objects.get(user=request.user)
            return render(request,'leave_portal/authorized_dashboard.html',{'user':request.user , 'authorized':authorized})

    elif request.user.person=='faculty':
        faculty = models.Faculty.objects.filter(user=request.user)
        if not faculty :
            form = forms.UpdateFacultyDetail()
            if request.method=='POST' :
                form = forms.UpdateFacultyDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('leave_portal:dashboard')
            else :
                return render(request,'leave_portal/dppc_update_detail.html', {'form':form , 'dppc':request.user.username} )
        else:
            authorized = models.Faculty.objects.get(user=request.user)
            return render(request,'leave_portal/authorized_dashboard.html',{'user':request.user , 'authorized':authorized})











#--------------------------------------------------------------

def index(request):
    return HttpResponse("HelloWorld!!")

class StudentListView(generic.ListView):
    model = models.CustomUser
    context_object_name = 'student_list'
    queryset = CustomUser.objects.filter(person__iexact='student') # Get 5 books containing the title war
    template_name = 'leave_portal/student_list.html'


class StudentDetailView(generic.DetailView):
    model = models.Student

class ApplyLeaveDetailView(generic.DetailView):
    model = models.ApplyLeave



def ApplyLeave(request,pk):
    student = get_object_or_404(models.Student, pk=pk)
    form = forms.LeaveForm()

    if request.method == 'POST':
        form = forms.LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            # print(leave.SentTo)
            leave.student = student

            if '1' in leave.SentTo:
                leave.flag=1

            if '2' in leave.SentTo and leave.flag is 0:
                leave.flag=2

            if '3' in leave.SentTo:
                leave.flag=3

            leave.save()
            return HttpResponseRedirect(student.get_absolute_url())
    return render(request, 'leave_portal/leaveform.html', {'student':student, 'form':form})



#change flag accordingly

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

class DppcListView(generic.ListView):
    model = models.Dppc

class DppcDetailView(generic.DetailView):
    model = models.Dppc


def DppcUpdateDetail(request, pk):
    dppc = get_object_or_404(models.Dppc, pk=pk)
    form = forms.UpdateDppcDetail(instance=dppc)

    if request.method == 'POST':
        form = forms.UpdateDppcDetail(instance=dppc, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(dppc.get_absolute_url())

    return render(request, 'leave_portal/dppc_update_detail.html', {'form':form, 'authorized':dppc})

def HodUpdateDetail(request, pk):
    hod = get_object_or_404(models.Hod, pk=pk)
    form = forms.UpdateHodDetail(instance=hod)

    if request.method == 'POST':
        form = forms.UpdateHodDetail(instance=hod, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(hod.get_absolute_url())

    return render(request, 'leave_portal/dppc_update_detail.html', {'form':form, 'authorized':hod})

def StaffUpdateDetail(request, pk):
    staff = get_object_or_404(models.Staff, pk=pk)
    form = forms.UpdateStaffDetail(instance=staff)

    if request.method == 'POST':
        form = forms.UpdateStaffDetail(instance=staff, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(staff.get_absolute_url())

    return render(request, 'leave_portal/dppc_update_detail.html', {'form':form, 'authorized':faculty})

def FacultyUpdateDetail(request, pk):
    faculty = get_object_or_404(models.Faculty, pk=pk)
    form = forms.UpdateFacultyDetail(instance=faculty)

    if request.method == 'POST':
        form = forms.UpdateFacultyDetail(instance=faculty, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(faculty.get_absolute_url())

    return render(request, 'leave_portal/dppc_update_detail.html', {'form':form, 'authorized':faculty})


def PendingRequest(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    forms = models.ApplyLeave.objects.filter(student=student,ApprovedStatus='pending')
    return render(request, 'leave_portal/pending_request.html', {'forms':forms})

def History(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    forms = models.ApplyLeave.objects.filter(student=student)
    return render(request, 'leave_portal/history.html', {'forms':forms})


def authorized_pending(request):
    if request.user.person == 'dppc':
        forms=models.ApplyLeave.objects.filter(flag=3,ApprovedStatus='pending')

    elif request.user.person == 'faculty' :

        forms1=models.ApplyLeave.objects.filter(student__TA_instructor__user=request.user ,flag=1,ApprovedStatus__iexact='pending')
        forms2=models.ApplyLeave.objects.filter(student__Supervisor_1__user=request.user ,flag=2,ApprovedStatus__iexact='pending')
        forms=forms1 | forms2

    elif request.user.person == 'hod':
        forms=models.ApplyLeave.objects.filter(flag=5,ApprovedStatus__iexact='pending')

    elif request.user.person == 'staff':
        forms=models.ApplyLeave.objects.filter(flag=4,ApprovedStatus__iexact='pending')

    return render(request, 'leave_portal/authorized_pending_request.html',{'forms':forms})

def approveleave(request, pk):
    form = get_object_or_404(models.ApplyLeave , pk=pk)

    if form.flag is 5:
        form.ApprovedStatus='approved'

    if form.flag < 4 :
        if '1' in form.SentTo and '2' in form.SentTo:
            if form.flag is 1:
                form.flag=2
            else:
                form.flag=4
        elif '1' in form.SentTo or '2' in form.SentTo:
            form.flag=4

        elif '3' in form.SentTo:
            form.flag=4

    else:
        form.flag+=1

    form.save()
    return redirect('leave_portal:dashboard')


def declineleave(request, pk):
    form = get_object_or_404(models.ApplyLeave , pk=pk)
    form.ApprovedStatus='declined'
    form.save()
    return redirect('leave_portal:dashboard')


#
#
# def declineleave(request, pk):
#     leave = get_object_or_404(models.ApplyLeave, pk=pk)
#
#     if request.method == 'POST':
#         comment=get_object_or_404(models.Comments,pk=request.id)
#         # comment=models.Comments.objects.filter(Leave=leave)
#         # form = forms.CommentsForm(instance=comment, data=request.POST)
#         if form.is_valid():
#             leave =
#             form.save()
#         leave.ApprovedStatus='declined'
#         leave.save()
#         return HttpResponse('done')
#
#     # form = forms.CommentsForm()
#     # return render(request, 'leave_portal/comments.html', {'form':form, 'leave':leave})
