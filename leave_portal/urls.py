from django.urls import path,include
from . import views

app_name = "leave_portal"
urlpatterns = [
    path('',views.index),
    path('student',views.StudentListView.as_view() , name="studentsList" ),
    # path('students/<int:pk>',views.tatti),
    path('student/<int:pk>',views.StudentDetailView.as_view(), name="studentsDetail" ),
    path('student/leaveform/<int:pk>', views.ApplyLeave, name="apply_leave"),
    path('student/leaveform/<int:pk>/<int:leave_id>', views.ApplyLeaveEdit, name="apply_leave_edit"),
]
