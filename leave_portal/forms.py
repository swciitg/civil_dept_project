from . import models
from django import forms


class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.ApplyLeave
        fields = ['LeaveFrom','LeaveTo','ReasonForLeave','AddressWhileOnLeave','PhoneNumberWhileOnLeave','DateOfApply','TypeOfLeave','Doc1','Doc2','SentTo']


class UpdateStudLeave(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            'Medical',
            'Ordinary',
            'conference',
            'sample_Collection'
        ]

class UpdateStudDetail(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            'profile_pic',
            'name',
            'roll_no',
            'gender',
            'webmail',
            'course',
            'acedemic_year',
            'present_semester',
            'hostel_name',
            'room_number',
            'mob_number',
            'emergency_mob_num',
            'TA_instructor',
            'Supervisor_1',
        ]


class UpdateDppcDetail(forms.ModelForm):
    class Meta:
        model = models.Dppc
        fields = [
            'profile_pic',
            'name',
            'webmail',
            'mob_num',
            'dppc_id',
        ]

class UpdateHodDetail(forms.ModelForm):
    class Meta:
        model = models.Hod
        fields = [
            'profile_pic',
            'name',
            'webmail',
            'mob_num',
            'hod_id',
        ]

class UpdateStaffDetail(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = [
            'profile_pic',
            'name',
            'webmail',
            'mob_num',
            'staff_id',
        ]

class UpdateFacultyDetail(forms.ModelForm):
    class Meta:
        model = models.Faculty
        fields = [
            'profile_pic',
            'name',
            'webmail',
            'mob_num',
            'faculty_id',
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = [
            'Remark',
        ]
