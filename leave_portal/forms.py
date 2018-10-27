from . import models
from django import forms


class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.ApplyLeave
        fields = ['LeaveFrom','LeaveTo','TypeOfLeave','ReasonForLeave','Doc1','Doc2','AddressWhileOnLeave','PhoneNumberWhileOnLeave','DateOfApply','Flag','SentTo']
