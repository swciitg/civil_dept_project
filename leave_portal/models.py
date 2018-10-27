from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from _datetime import datetime
from django.urls import reverse

# Create your models here.

HOSTEL_CHOICES = (
    ('Barak', 'Barak'),
    ('Bramhaputra', 'Bramhaputra'),
    ('Dhansiri', 'Dhansiri'),
    ('Dibang', 'Dibang'),
    ('Dihing', 'Dihing'),
    ('Kameng', 'Kameng'),
    ('Kapili', 'Kapili'),
    ('Lohit', 'Lohit'),
    ('Manas', 'Manas'),
    ('Siang', 'Siang'),
    ('Subansiri', 'Subansiri'),
    ('Umiam', 'Umiam'),
    ('Married_Scholar', 'Married_Scholar'),
    ('NA', 'NA'),

)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

TYPEOFLEAVE = (
    ('Ordinary', 'Ordinary'),
    ('Medical', 'Medical'),
    ('Acedemic', 'Acedemic'),
    ('Maternity', 'Maternity'),
    ('Paternity', 'Paternity')
)
COURSE = (
    ('Mtech', 'Mtech'),
    ('Phd', 'Phd'),
    ('NA', 'NA')
)

ACADEMIC_YEAR = (
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
    (6, ("6")),
    (7, ("7")),
)

SEMESTER = (
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
    (6, ("6")),
    (7, ("7")),
)

SENT_TO = (('1', 'Supervisor'),
           ('2', 'TAinstructor'),
           ('3', 'DPPC'))

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_office = models.BooleanField(default=False)
    is_dppc = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=200, blank=True, default="")
    profile_pic = models.ImageField(upload_to='student', blank=True, null=True)
    roll_no = models.CharField(max_length=128, blank=False, default=" ", unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=False)
    webmail = models.CharField(max_length=128, blank=False, unique=True)
    course = models.CharField(max_length=128, choices=COURSE, blank=True)
    acedemic_year = models.IntegerField(choices=ACADEMIC_YEAR, default=0)
    present_semester = models.IntegerField(choices=SEMESTER, null=True, blank=True)
    hostel_name = models.CharField(max_length=255, choices=HOSTEL_CHOICES, blank=True, default="")
    room_number = models.CharField(max_length=10, blank=True, default="")
    mob_number = models.CharField(max_length=15, blank=False, default=" ")
    emergency_mob_num = models.CharField(max_length=15, blank=True, default=" ")
    TA_instructor = models.CharField(max_length=200, blank=True, default="", )
    Supervisor_1 = models.CharField(max_length=200, blank=True, default="")
    Ordinary = models.IntegerField( blank=False, default=15)
    Medical = models.IntegerField( blank=False, default=15)
    Acedemic = models.IntegerField( blank=False, default=30)
    Maternity = models.IntegerField( blank=False, default=135)
    Paternity = models.IntegerField( blank=False, default=15)

    class Meta:
        ordering =['roll_no']

    def get_absolute_url(self):
        return reverse('leave_portal:studentsDetail',kwargs={'pk':self.id})

    def __str__(self):
        return self.name

class Authorized(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    profile_pic = models.ImageField(upload_to='faculty', blank=True, null=True, default=" ")
    webmail = models.CharField(max_length=128, blank=False)
    mob_num = models.CharField(max_length=128, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Faculty(Authorized):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')
    faculty_id = models.CharField(max_length=128, blank=False)

class Dppc(Authorized):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dpppc')
    dppc_id = models.CharField(max_length=128, blank=False)

class Hod(Authorized):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hod')
    hod_id = models.CharField(max_length=128, blank=False)

class Staff(Authorized):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff')
    staff_id = models.CharField(max_length=128, blank=False)

class ApplyLeave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='applyleaves')
    LeaveFrom = models.DateField()
    LeaveTo = models.DateField()
    TypeOfLeave = models.CharField(max_length=255, choices=TYPEOFLEAVE, blank=False, default="")
    ReasonForLeave = models.CharField(max_length=200)
    Doc1 = models.FileField(upload_to='documents', blank=True, null=True)
    Doc2 = models.FileField(upload_to='documents', blank=True, null=True)
    AddressWhileOnLeave = models.CharField(max_length=200)
    PhoneNumberWhileOnLeave = models.CharField(max_length=20)
    DateOfApply = models.DateField(default=datetime.now)
    Flag = models.IntegerField(default=0)
    SentTo = MultiSelectField(choices=SENT_TO)

    def __str__(self):
        return self.student.name


class Comments(models.Model):
    Leave = models.ForeignKey(ApplyLeave, on_delete=models.CASCADE, related_name='comments')
    Remark = models.CharField(max_length=200)
    Person = models.CharField(max_length=40)
    DateOfComment = models.DateField(default=datetime.now)

    def __str__(self):
        return self.Person
