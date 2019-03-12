from django.urls import path,include
from . import views

app_name = "leave_portal"
urlpatterns = [
    path('',views.index , name="HelloWorld"),

    path('dashboard', views.dashboard , name='dashboard'),
    path('dppc/updatedppcdata/<int:pk>',views.DppcUpdateDetail, name="dppc_detail_update"),
    path('hod/updatehoddata/<int:pk>',views.HodUpdateDetail, name="hod_detail_update"),
    path('staff/updatestaffdata/<int:pk>',views.StaffUpdateDetail, name="staff_detail_update"),
    path('faculty/updatefacultydata/<int:pk>',views.FacultyUpdateDetail, name="faculty_detail_update"),

    path('<int:pk>' , views.ApplyLeaveDetailView.as_view() , name="leave_info"),

    path('student',views.StudentListView.as_view() , name="studentsList" ),
    path('students/updatedata/<int:pk>',views.StudentUpdateDetail, name="stud_detail_update"),
    path('student/<int:pk>',views.StudentDetailView.as_view(), name="studentsDetail" ),
    path('student/leaveform/<int:pk>', views.ApplyLeave, name="apply_leave"),
    path('student/leaveform/<int:pk>/<int:leave_id>', views.ApplyLeaveEdit, name="apply_leave_edit"),
    path('student/<int:pk>/pending', views.PendingRequest,name="pending_request"),
    path('student/<int:pk>/history', views.History,name="history"),
    path('authorized/pending_request',views.authorized_pending,name="authorized_pending_request"),
    path('authorized/pending_request/approve/<int:pk>',views.approveleave,name="Approve"),
    path('authorized/pending_request/decline/<int:pk>',views.declineleave,name="Decline"),
    path('dppc',views.DppcListView.as_view(), name="dppclist"),
    path('dppc/<int:pk>',views.DppcDetailView.as_view(), name="dppcdetail"),



]
