from . import models
from django import forms


class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.ApplyLeave
        fields = ['LeaveFrom','LeaveTo','TypeOfLeave','ReasonForLeave','Doc1','Doc2','AddressWhileOnLeave','PhoneNumberWhileOnLeave','DateOfApply','Flag','SentTo']


class UpdateStudDetail(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            'name',
            'profile_pic',
            'roll_no',
            'gender',
            'webmail',
            'course',
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
            'name',
            'profile_pic',
            'webmail',
            'mob_num',
            'dppc_id',
        ]

class UpdateHodDetail(forms.ModelForm):
    class Meta:
        model = models.Hod
        fields = [
            'name',
            'profile_pic',
            'webmail',
            'mob_num',
            'hod_id',
        ]

class UpdateStaffDetail(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = [
            'name',
            'profile_pic',
            'webmail',
            'mob_num',
            'staff_id',
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = [
            'Remark',
        ]
