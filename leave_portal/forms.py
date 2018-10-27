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
