from django.urls import path,include
from . import views

app_name = "leave_portal"
urlpatterns = [
    path('',views.index),
    path('student',views.StudentListView.as_view() , name="studentsList" ),
    path('students/updatedata/<int:pk>',views.StudentUpdateDetail, name="stud_detail_update"),
    path('student/<int:pk>',views.StudentDetailView.as_view(), name="studentsDetail" ),
    path('student/leaveform/<int:pk>', views.ApplyLeave, name="apply_leave"),
    path('student/leaveform/<int:pk>/<int:leave_id>', views.ApplyLeaveEdit, name="apply_leave_edit"),
    path('student/<int:pk>/pending', views.PendingRequest,name="pending_request")
]
